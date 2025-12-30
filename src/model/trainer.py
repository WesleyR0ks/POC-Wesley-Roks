import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from joblib import dump

from pipeline.text_processing import clean_text

# Load data
data = pd.read_csv("../data/emails.csv")

# Preprocess
data["text"] = data["text"].apply(clean_text)
data["label"] = data["label"].map({"legitimate": 0, "phishing": 1})

X = data["text"]
y = data["label"]

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# Evaluate on training data
predictions = model.predict(X_vec)
accuracy = accuracy_score(y, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Save
dump(model, "phishing_model.pkl")
dump(vectorizer, "vectorizer.pkl")
