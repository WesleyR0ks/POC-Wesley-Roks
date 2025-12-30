from joblib import load
from pipeline.text_processing import clean_text

model = load("model/phishing_model.pkl")
vectorizer = load("model/vectorizer.pkl")

def predict_email(text: str) -> str:
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    return "PHISHING" if prediction == 1 else "LEGITIMATE"