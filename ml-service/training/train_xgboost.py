import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)

from xgboost import XGBClassifier

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("dataset/processed_fraud.csv")

X = df.drop(columns=["Fraudulent"])
y = df["Fraudulent"]

# ==========================
# Train Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# ==========================
# Scale Numerical Features
# ==========================

numeric_columns = [
    "Transaction_Amount",
    "Time_of_Transaction",
    "Previous_Fraudulent_Transactions",
    "Account_Age",
    "Number_of_Transactions_Last_24H",
]

scaler = StandardScaler()

X_train[numeric_columns] = scaler.fit_transform(
    X_train[numeric_columns]
)

X_test[numeric_columns] = scaler.transform(
    X_test[numeric_columns]
)

# ==========================
# XGBoost
# ==========================

model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="binary:logistic",
    eval_metric="logloss",
    random_state=42,
)

model.fit(X_train, y_train)

# ==========================
# Predictions
# ==========================

predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print("\n========== METRICS ==========\n")

print(f"Accuracy  : {accuracy_score(y_test, predictions):.4f}")
print(f"Precision : {precision_score(y_test, predictions, zero_division=0):.4f}")
print(f"Recall    : {recall_score(y_test, predictions, zero_division=0):.4f}")
print(f"F1 Score  : {f1_score(y_test, predictions, zero_division=0):.4f}")
print(f"ROC AUC   : {roc_auc_score(y_test, probabilities):.4f}")

print("\n========== CONFUSION MATRIX ==========\n")
print(confusion_matrix(y_test, predictions))

print("\n========== CLASSIFICATION REPORT ==========\n")
print(classification_report(y_test, predictions, zero_division=0))

joblib.dump(model, "models/xgboost_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("\n✅ XGBoost model saved!")