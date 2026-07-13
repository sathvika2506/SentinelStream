import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("dataset/fraud.csv")

print("Original Shape:", df.shape)

# -----------------------
# Drop Transaction_ID
# -----------------------
df = df.drop(columns=["Transaction_ID"])

# -----------------------
# Fill Missing Values
# -----------------------

# Numerical columns
num_cols = [
    "Transaction_Amount",
    "Time_of_Transaction"
]

num_imputer = SimpleImputer(strategy="median")
df[num_cols] = num_imputer.fit_transform(df[num_cols])

# Categorical columns
cat_cols = [
    "Device_Used",
    "Location",
    "Payment_Method",
    "Transaction_Type"
]

cat_imputer = SimpleImputer(strategy="most_frequent")
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

# -----------------------
# Encode Categories
# -----------------------

encoders = {}

for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

print("\nProcessed Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nPreview:")
print(df.head())

# Save processed dataset
df.to_csv("dataset/processed_fraud.csv", index=False)

print("\n✅ Saved dataset as dataset/processed_fraud.csv")