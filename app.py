from flask import Flask, render_template, request, jsonify
import requests

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


if __name__ == "__main__":
    app.run(debug=True)
