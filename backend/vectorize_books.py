from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Simulate reading books from Project Gutenberg
book1 = "The summary of book 1..."
book2 = "The content, content, content of book 2..."


books = [book1, book2]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(books)

# Save the vectorizer and the vectorized books for future use
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("vectorized_books.pkl", "wb") as f:
    pickle.dump(X, f)

