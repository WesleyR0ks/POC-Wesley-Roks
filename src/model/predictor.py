from pathlib import Path
from joblib import load
from pipeline.text_processing import clean_text

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "phishing_model.pkl"
VECTORIZER_PATH = BASE_DIR / "vectorizer.pkl"

model = load(MODEL_PATH)
vectorizer = load(VECTORIZER_PATH)


def predict_email(text: str) -> str:
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    return "PHISHING" if prediction == 1 else "LEGITIMATE"
