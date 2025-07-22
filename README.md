<h1 align="center">🎬 Movie Recommender System</h1>

<p align="center">
  An intelligent movie recommendation system built with <b>Python, Machine Learning, Streamlit</b>, and <b>TMDB API</b>.
  <br><br>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=flat&logo=streamlit">
  <img src="https://img.shields.io/badge/ML-Recommendation-blueviolet">
  <img src="https://img.shields.io/badge/TMDB-API-yellowgreen?logo=themoviedatabase">
</p>

---

## 🚀 Overview

This project recommends **5 similar movies** when you select one from the dropdown — and shows their **posters** in a beautifully styled interface using **TMDB API**.

Built as a part of my ML learning journey, this app combines:
- 🔍 Cosine Similarity
- 🧠 Content-Based Filtering
- ⚡️ Fast, interactive frontend (via Streamlit)

> **Try it yourself and get your next favorite movie suggestion!**

---

## 🧠 How It Works

1. User selects a movie
2. System finds its index in the movie list
3. Uses **precomputed cosine similarity matrix** to find top 5 similar movies
4. Displays everything in a clean, responsive layout 🎨

---

## 🗂 Files in this Repo

| File Name              | Purpose |
|------------------------|---------|
| `app.py`               | Main Streamlit web app code |
| `movie_list.pkl`       | Preprocessed movie titles + TMDB IDs |
| `similarity.pkl`       | Cosine similarity matrix |
| `tmdb_5000_movies.csv` | Raw movie metadata (title, genre, etc.) |
| `tmdb_5000_credits.csv`| Raw cast/crew data |
| `requirements.txt`     | Python packages required |
| `README.md`            | You're reading it 😉 |

---

## 💻 Run Locally

```bash
# Clone this repo
git clone https://github.com/yourusername/movie-recommender-system
cd movie-recommender-system

# Create virtual env (optional)
python -m venv venv
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
