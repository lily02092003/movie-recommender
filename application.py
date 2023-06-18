import streamlit as st
import pickle
import pandas as pd
import requests
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=fbca03ae512501000b0e1abab98c7121"
    response = requests.get(url)
    movie_details = response.json()
    return movie_details
def get_movie_details1(movie_id):
    movie_details = get_movie_details(movie_id)
    return "http://image.tmdb.org/t/p/w500/" + movie_details['poster_path']
def recommend(movie):
      #fetch index of movie
      movie_index=movies[movies['title'] == movie].index[0]
      #fetching similarity of movie with other movies from similarity matrix
      distance=similarity[movie_index]
      movie_recommend=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
      recommended=[]
      re_poster=[]
      for i in movie_recommend:
          movie_id=movies.iloc[i[0]].movie_id
          recommended.append(movies.iloc[i[0]].title)
          re_poster.append(get_movie_details1(movie_id))
      return recommended,re_poster

st.title("Movie recommender system")
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
movie_selected = st.selectbox(
    'Choose your movie for which you want to get recommendations',
    movies['title'].values)
press_button = st.button('Recommend Me')
names, posters = recommend(movie_selected)
if press_button:
    show_second_button=True
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        movie_index = movies[movies['title'] == names[0]].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        movie_details = get_movie_details(movie_id)
        st.text(names[0])
        st.image(posters[0])
        st.write("Overview:", movie_details["overview"])
        st.write("Release Date:", movie_details["release_date"])

    with col2:
        movie_index = movies[movies['title'] == names[1]].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        movie_details = get_movie_details(movie_id)
        st.text(names[1])
        st.image(posters[1])
        st.write("Overview:", movie_details["overview"])
        st.write("Release Date:", movie_details["release_date"])
    with col3:
        movie_index = movies[movies['title'] == names[2]].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        movie_details = get_movie_details(movie_id)
        st.text(names[2])
        st.image(posters[2])
        st.write("Overview:", movie_details["overview"])
        st.write("Release Date:", movie_details["release_date"])
    with col4:
        movie_index = movies[movies['title'] == names[3]].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        movie_details = get_movie_details(movie_id)
        st.text(names[3])
        st.image(posters[3])
        st.write("Overview:", movie_details["overview"])
        st.write("Release Date:", movie_details["release_date"])
    with col5:
        movie_index = movies[movies['title'] == names[4]].index[0]
        movie_id = movies.iloc[movie_index].movie_id
        movie_details = get_movie_details(movie_id)
        st.text(names[4])
        st.image(posters[4])
        st.write("Overview:", movie_details["overview"])
        st.write("Release Date:", movie_details["release_date"])