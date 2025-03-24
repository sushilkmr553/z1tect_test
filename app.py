import streamlit as st
import requests

# OMDB API Key
OMDB_API_KEY = "c7ec0b49"

# Streamlit App Title
st.title("🎬 Movie Search App")

# Search Input
query = st.text_input("Search for a movie:", "")

if st.button("Search"):
    if not query:
        st.error("Please enter a search query.")
    else:
        url = f"http://www.omdbapi.com/?s={query}&apikey={OMDB_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            movies = data["Search"]
            for movie in movies:
                st.image(movie["Poster"], width=150)
                st.subheader(movie["Title"])
                st.write(f"📅 Year: {movie['Year']}")
                st.write(f"🔎 [View Details](?movie_id={movie['imdbID']})")

        else:
            st.error(data.get("Error", "No results found."))

# Movie Details Section
if "movie_id" in st.query_params:
    movie_id = st.query_params["movie_id"]
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        st.image(data["Poster"], width=200)
        st.subheader(data["Title"])
        st.write(f"📅 Year: {data['Year']}")
        st.write(f"🎭 Genre: {data['Genre']}")
        st.write(f"⭐ IMDB Rating: {data['imdbRating']}")
        st.write(f"🎬 Director: {data['Director']}")
        st.write(f"📝 Plot: {data['Plot']}")
    else:
        st.error("Movie not found.")
