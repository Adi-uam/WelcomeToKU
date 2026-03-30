import joblib
import numpy as np

model = joblib.load("app/ml/model.pkl")

def predict_grant_probability(gpa: float, ent_score: int):
    features = np.array([[gpa, ent_score]])
    prob = model.predict_proba(features)[0][1]
    return round(prob * 100, 2)