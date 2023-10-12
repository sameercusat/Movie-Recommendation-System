import streamlit as st
import pickle
import pandas as pd
import requests

def  fetch_poster(movie_id):
    response=requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies ,recommended_movies_poster
st.title("Movie Recommender System")
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('simi.pkl','rb'))
movies=pd.DataFrame(movie_dict)
#print(movies.head(10))
option=st.selectbox("Select your Movie",movies['title'].values)
if st.button("Recommend"):
    names,poster=recommend(option)
    col0,col1,col2,col3,col4=st.columns(5)
    with col0:
        st.text(names[0])
        st.image(poster[0])
    with col1:
        st.text(names[1])
        st.image(poster[1])    
    with col2:
        st.text(names[2])
        st.image(poster[2])   
    with col3:
        st.text(names[3])
        st.image(poster[3])
    with col4:
        st.text(names[4])
        st.image(poster[4])         

    
