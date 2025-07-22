# 🎬 Movie Recommendation System

A **content-based movie recommender system** that suggests movies based on similarity in genres, cast, and keywords using **cosine similarity**. The project is built with **Python**, **Pandas**, **Scikit-learn**, and deployed using **Streamlit** for interactive web-based access.

🌐 **Live Demo:**  
👉 [Try the App Here](https://netblix-app-sxuswdzh2digmutyz8mv5d.streamlit.app/)

---

## 🚀 Features

- Search for any movie and get a list of similar movies instantly
- Uses **content-based filtering** via **cosine similarity**
- Vectorization using **CountVectorizer**
- Built with **Streamlit** for real-time interaction
- Lightweight, fast, and easy to use

---

## 🧠 How It Works

1. Extract metadata from the dataset (genres, cast, crew, keywords)
2. Combine features into a single text-based "tags" column
3. Convert text into numerical vectors using **CountVectorizer**
4. Compute similarity scores using **cosine similarity**
5. Return top 5 most similar movies based on the selected input

---

## 📊 Dataset

- Based on TMDB movie dataset
- Contains movie titles, overviews, genres, keywords, cast, and crew info

---

## 🛠️ Tech Stack

- Python
- Pandas, Numpy
- Scikit-learn
- Streamlit
- CountVectorizer (for feature extraction)
- Cosine Similarity (for recommendation)

---

## 🖥️ How to Run Locally

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run app.py
