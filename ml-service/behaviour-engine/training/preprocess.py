import pandas as pd
import joblib

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("dataset/behavior_dataset.csv")

print("Original Shape:", df.shape)

# -------------------------
# Drop almost-empty columns
# -------------------------

df = df.drop(columns=[
    "swipe_speed_avg",
    "double_click"
])

# -------------------------
# Fill missing values
# -------------------------

numeric_cols = [
    "error_rate",
    "tilt_angle_avg"
]

imputer = SimpleImputer(strategy="median")

df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

# -------------------------
# Encode pressure_touch
# -------------------------

pressure_encoder = LabelEncoder()

df["pressure_touch"] = pressure_encoder.fit_transform(
    df["pressure_touch"].fillna("Unknown")
)

# -------------------------
# Encode Gender
# -------------------------

gender_encoder = LabelEncoder()

df["user.1"] = gender_encoder.fit_transform(df["user.1"])

# -------------------------
# Encode User Labels
# -------------------------

user_encoder = LabelEncoder()

df["user"] = user_encoder.fit_transform(df["user"])

print("\nProcessed Shape:", df.shape)

print("\nMissing Values")
print(df.isnull().sum())

df.to_csv("dataset/behavior_processed.csv", index=False)

joblib.dump(user_encoder, "models/user_encoder.pkl")

print("\n Saved processed dataset")
print(" Saved label encoder")