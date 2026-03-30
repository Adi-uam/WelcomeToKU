import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.DataFrame({
    "gpa": [3.5, 3.8, 2.9, 3.2, 3.9, 2.5],
    "ent_score": [110, 125, 90, 100, 130, 80],
    "grant": [1, 1, 0, 0, 1, 0]
})

X = data[["gpa", "ent_score"]]
y = data["grant"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "app/ml/model.pkl")

print("Model trained and saved!")