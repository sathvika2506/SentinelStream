import pandas as pd

df = pd.read_csv("dataset/dataset.csv")

print("=" * 60)
print("Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nFirst 5 Rows")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())