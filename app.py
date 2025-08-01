import os
import urllib.request
import pickle
import streamlit as st
import requests
import time

def download_similarity_file():
    url = "https://www.dropbox.com/scl/fi/8jdlz3c0t1bb20v7o40c3/similarity.pkl?rlkey=lt4q4br6yccvwl886bmy01fl9&st=n2d5cre4&dl=1"
    output = "similarity.pkl"
    try:
        urllib.request.urlretrieve(url, output)
        print("similarity.pkl downloaded from Dropbox")
    except Exception as e:
        st.error(f"Error downloading similarity.pkl: {e}")

if not os.path.exists("similarity.pkl"):
    download_similarity_file()

movies = pickle.load(open('movie_list.pkl', 'rb'))  
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    api_key = "c7385d9faab6ffabaf38b1f824a8b343"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    time.sleep(2)
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        time.sleep(1)
        movie_id = movies.iloc[i[0]].id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names, recommended_movie_posters

st.header('🎬 Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        # st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        # st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        # st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        # st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        # st.image(recommended_movie_posters[4])
