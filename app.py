from flask import Flask, render_template, request, jsonify
import requests
import streamlit as st

app = Flask(__name__)
OMDB_API_KEY = "c7ec0b49"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    url = f"http://www.omdbapi.com/?s={query}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(data)

    if data.get("Response") == "True":
        return jsonify(data["Search"])
    else:
        return jsonify({"error": data.get("Error", "No results found")}), 404


@app.route("/movie/<movie_id>", methods=["GET"])
def movie_detail(movie_id):
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return jsonify(data)
    else:
        return jsonify({"error": data.get("Error", "Movie not found")}), 404


def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

# Start Flask server
thread = threading.Thread(target=run_flask)
thread.daemon = True
thread.start()

# Streamlit App
st.title("Streamlit with Flask")
st.write("Flask is running in the background!")