from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import pickle
from flask_cors import CORS
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__, static_folder="static", template_folder="templates")

CORS(app, resources={r"/search": {"origins": "*"}})

# Load the vectorizer and the vectorized books
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("vectorized_books.pkl", "rb") as f:
    X = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<path:path>")
def static_file(path):
    return send_from_directory("static", path)

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query")
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, X)
    most_similar_book_index = similarities.argmax()
    print(most_similar_book_index)
    return jsonify({"most_similar_book": int(most_similar_book_index)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
