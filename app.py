import streamlit as st
import pickle
import requests  #library used for sending request to api 

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=160e5ff85dd6ce0a399f97324c93a4fd'.format(movie_id))
    movie_data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+movie_data['poster_path']  #complete poster path
    


similarity=pickle.load(open('similarity.pkl','rb'))

#function giving recommended movies

def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[0:5]
    
    recommended_movies=[]  #list for storing list of recommended movies
    recommended_movies_posters=[]  #list for storing posters of recommended movies

    for i in movies_list:
        movies_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))  #fetch_poster returns complete poster path of each movie 
    return recommended_movies,recommended_movies_posters


movies=pickle.load(open('movies.pkl','rb'))
movie_list=movies['title'].values

st.header("movie recommendation system")

selected_movie_name=st.selectbox(
    'Which movie want?',
    (movie_list))

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    
    col1, col2,col3,col4,col5=st.columns(5)

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