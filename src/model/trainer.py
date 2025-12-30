# python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier
from joblib import dump

from pipeline.text_processing import clean_text

data = pd.read_csv("../data/emails.csv")

# Defensive checks
required_cols = {"text", "label"}
if not required_cols.issubset(data.columns):
    raise SystemExit(f"Missing required columns: {required_cols - set(data.columns)}")

# Normalize and map labels
data["text"] = data["text"].astype(str)
data["label"] = data["label"].astype(str).str.strip().str.lower()
label_map = {"legitimate": 0, "phishing": 1}
data["label_num"] = data["label"].map(label_map)

# Clean text and drop bad rows
data["text_clean"] = data["text"].apply(clean_text)
data = data[data["text_clean"].str.len() > 0]
data = data.dropna(subset=["label_num"])

print("Class distribution (after cleaning):")
print(data["label_num"].value_counts())

if data.shape[0] == 0:
    raise SystemExit("No data left after cleaning. Check `../data/emails.csv` and `clean_text` behavior.")

X = data["text_clean"]
y = data["label_num"].astype(int)

# Vectorize
vectorizer = TfidfVectorizer(stop_words="english", max_features=20000)
X_vec = vectorizer.fit_transform(X)

# Decide whether to stratify (require at least one sample per class in train/test)
stratify_arg = y if y.nunique() > 1 and (y.value_counts().min() >= 2) else None
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42, stratify=stratify_arg
)

# Handle class imbalance for XGBoost
neg = int((y_train == 0).sum())
pos = int((y_train == 1).sum())
scale_pos_weight = (neg / pos) if pos > 0 else 1.0
print(f"Train classes: neg={neg}, pos={pos}, scale_pos_weight={scale_pos_weight:.2f}")

# Train model (omit deprecated `use_label_encoder`)
model = XGBClassifier(
    n_estimators=100,
    objective="binary:logistic",
    eval_metric="logloss",
    scale_pos_weight=scale_pos_weight
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2f}")
print(classification_report(y_test, predictions, zero_division=0))

# Save model & vectorizer
dump(model, "phishing_model.pkl")
dump(vectorizer, "vectorizer.pkl")
