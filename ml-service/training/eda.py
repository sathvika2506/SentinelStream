import pandas as pd

df = pd.read_csv("dataset/processed_fraud.csv")

print(df["Fraudulent"].value_counts())
print(df["Fraudulent"].value_counts(normalize=True))