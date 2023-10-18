# Project Gutenberg Book Search API

**Project Gutenberg Book Search API** is an interview project designed to challenge candidates on various aspects of software development, from understanding basic backend development with Flask to advanced topics in Natural Language Processing (NLP). This project leverages a basic implementation, providing candidates with a foundation to build upon.

## **Table of Contents**

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)

## **Features**

- **TF-IDF Vectorization**: Uses the Term Frequency-Inverse Document Frequency method to transform book content into vectors.
- **Cosine Similarity**: Compares user query with stored books to find the closest match.
- **Flask Backend**: Utilizes Flask to handle incoming requests and deliver responses.
- **Cross-Origin Support**: Incorporates CORS to facilitate integration with various frontends.


## **Prerequisites**

Ensure you have:

- Python 3.x
- Required Python libraries: Flask, scikit-learn, flask-cors

Install the dependencies with:
```bash
pip install Flask scikit-learn flask-cors
```

## **Getting Started**

1. **Vectorizing Books**:
    - Execute the `vectorize_books.py` script to preprocess the book data.
   ```bash
   python vectorize_books.py
   ```
   This will generate `vectorizer.pkl` and `vectorized_books.pkl`.

2. **Launching the API**:
    - Initiate the Flask server using `search_api.py`.
   ```bash
   python search_api.py
   ```
   The API will be available at `http://localhost:5000`.

## **Usage**

POST to the `/search` endpoint with your query:

```json
{
    "query": "Your search term here"
}
```

Response:

```json
{
    "most_similar_book": 0
}
```