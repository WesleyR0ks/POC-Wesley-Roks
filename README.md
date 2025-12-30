# POC Wesley Roks

## Phishing Email Detection – Proof of Concept

### Overview
This repository contains a **Proof of Concept (PoC)** for detecting phishing emails using **Supervised Machine Learning** and **Natural Language Processing (NLP)**.

The PoC demonstrates:
- How email content can be automatically analyzed
- How a machine learning model can classify emails as **phishing** or **legitimate**
- A clear application of the **Trainer–Predictor design pattern**
- A simple graphical user interface where users can paste email content and receive a classification result

This PoC was created as part of a comparative analysis of machine learning components and design patterns, with phishing detection as the primary use case.

---

### Goal of the PoC
The goal of this Proof of Concept is to:
- Validate that supervised learning is suitable for phishing email detection
- Show a working end-to-end ML pipeline (training → prediction → user interaction)
- Demonstrate practical ML skills in a realistic but manageable scope

The system focuses on **text-based email analysis**, using NLP techniques to extract features from email content.

---

### Machine Learning Approach

#### Supervised Learning
The PoC uses **supervised learning**, where the model is trained on labeled examples:
- `phishing`
- `legitimate`

Each email is transformed into numerical features using **TF-IDF vectorization**, after which a classifier predicts the label.

---

### Why Logistic Regression Instead of XGBoost?

During the analysis phase, **XGBoost** was identified as the most suitable model for phishing detection due to its:
- High accuracy
- Robustness
- Good performance on large datasets

However, for this Proof of Concept, the model was intentionally changed to **Logistic Regression**.

#### Reason for this decision
- The PoC uses a very small dataset
- XGBoost is optimized for larger datasets and performed poorly in this constrained scenario
- Logistic Regression performs much better on small, text-based datasets
- Logistic Regression is easier to interpret and debug in a PoC context

This decision does not contradict the analysis conclusion, but reflects a pragmatic engineering choice based on PoC constraints.

In a production environment with sufficient data, XGBoost or similar ensemble models would be preferred.

---

### Architecture & Design Patterns

#### Trainer–Predictor Pattern
The system separates:
- Training logic (`trainer.py`)
- Prediction logic (`predictor.py`)

This ensures:
- Better maintainability
- Clear separation of responsibilities
- Easier future model replacement

#### Data Pipeline Pattern
Text preprocessing is centralized and reused for:
- Training
- Prediction

This guarantees consistent feature generation and prevents training–prediction mismatches.

---

### User Interface
The PoC includes a **simple desktop GUI** built with Tkinter:
- Users paste an email into a text box
- The system classifies the email
- The result is shown as PHISHING or LEGITIMATE

The UI is intentionally minimal to keep the focus on the machine learning pipeline.

---

### Current Limitations
This PoC is intentionally simple and has some known limitations:
- Very small training dataset
- No confidence score shown to the user
- UI is functional but basic
- No persistence or logging of predictions

---

### Roadmap – Future Improvements

#### Machine Learning Improvements
- Replace Logistic Regression with XGBoost once sufficient training data is available
- Expand dataset using real-world phishing corpora
- Add confidence scores to predictions
- Introduce an unsupervised anomaly detection pre-filter (e.g. Isolation Forest)
- Perform proper train/test/validation splits
- Add model performance metrics (precision, recall, confusion matrix)

#### UI Improvements
- Show prediction confidence percentage
- Highlight suspicious words or phrases in the email text
- Improve layout and visual feedback
- Add a history view of scanned emails
- Convert the desktop UI to a web-based interface (Flask or FastAPI)

---

### Conclusion
This Proof of Concept successfully demonstrates that supervised machine learning combined with NLP is an effective approach for phishing email detection.

While Logistic Regression is used in this PoC due to practical constraints, the architecture and design patterns allow for easy replacement with more advanced models such as XGBoost in future iterations.

The PoC serves as a solid foundation for further development towards a production-ready phishing detection system.
