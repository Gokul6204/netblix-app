import streamlit as st
import pickle
import requests
import math
import os
import gdown

st.set_page_config(page_title="NETBLIX - Movie Recommendation System", layout="wide")
st.header(":red[NETBLIX] :clapper:", divider="red")
st.markdown("Your personal movie recommendation system!")

API_KEY = "8c67ffa31c5f2b01ea4fe075b4ff8ce4"
TMDB_POSTER_BASE_URL = "http://image.tmdb.org/t/p/w500/"
PLACEHOLDER_IMAGE_URL = "https://via.placeholder.com/500x750?text=No+Poster+Available"

def download_file_from_google_drive(FILE_ID, output_file):
    file_url = f"https://drive.google.com/uc?id={FILE_ID}"
    if not os.path.exists(output_file):
        with st.spinner(f"Downloading {output_file}..."):
            gdown.download(file_url, output_file, quiet=False)
            st.success(f"{output_file} downloaded successfully.")

download_file_from_google_drive("1f_BaefMswB-20x3V7D9GCQ5JUHjecPg7", "movie_recommondation_model.pkl")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        return TMDB_POSTER_BASE_URL + poster_path if poster_path else PLACEHOLDER_IMAGE_URL
    except Exception:
        return PLACEHOLDER_IMAGE_URL

def recommend(movie, movie_list, similarity):
    try:
        movie_index = movie_list[movie_list['title'].str.lower().str.strip() == movie.lower().strip()].index[0]
        similar_movies = sorted(enumerate(similarity[movie_index]), key=lambda x: x[1], reverse=True)
        
        recommended_movies_name = []
        recommended_movies_poster = []
        for i in similar_movies[1:21]:
            movie_id = movie_list.iloc[i[0]].id
            recommended_movies_poster.append(fetch_poster(movie_id))
            recommended_movies_name.append(movie_list.iloc[i[0]].title)
        return recommended_movies_poster, recommended_movies_name
    except IndexError:
        st.error("Movie not found in the database. Please try another movie.")
        return [], []

@st.cache_resource
def load_data():
    try:
        movie_list = pickle.load(open("movie_titles (1)", "rb"))
        similarity = pickle.load(open("similarity.pkl", "rb"))
        return movie_list, similarity
    except FileNotFoundError:
        st.error("Required data files not found. Please ensure the data files are available.")
        st.stop()

movie_list, similarity = load_data()

st.title("Movie Recommendation System")
selected_movie_name = st.selectbox(
    "Which movie would you like to watch?",
    movie_list["title"].values
)
if st.button("Search"):
    st.subheader(f"Recommendations for :blue[{selected_movie_name}]")
    recommended_movies_poster, recommended_movies_name = recommend(selected_movie_name, movie_list, similarity)
    
    if recommended_movies_name:
        num_columns = 5
        rows = math.ceil(len(recommended_movies_name) / num_columns)
        for row in range(rows):
            cols = st.columns(num_columns)
            for col_index in range(num_columns):
                movie_index = row * num_columns + col_index
                if movie_index < len(recommended_movies_name):
                    with cols[col_index]:
                        st.image(recommended_movies_poster[movie_index], use_container_width=True)
                        st.caption(recommended_movies_name[movie_index])
    else:
        st.warning("No recommendations available for the selected movie. Please try a different movie.")

st.markdown("---")
st.text("Developed by Gokul")
