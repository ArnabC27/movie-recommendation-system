import streamlit as st
import pickle
import pandas as pd
import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer c65468ccddfd0da3f4e047779a2a7655"
}


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c65468ccddfd0da3f4e047779a2a7655&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:12]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('sim_matrix.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    'What will you watch today?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[9])
        st.image(posters[9])
