import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from joblib import dump

from pipeline.text_preprocessing import clean_text

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

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Train model
model = XGBClassifier(
    use_label_encoder=False,
    eval_metric="logloss"
)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2f}")

# Save model & vectorizer
dump(model, "phishing_model.pkl")
dump(vectorizer, "vectorizer.pkl")
