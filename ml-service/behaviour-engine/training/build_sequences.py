import pandas as pd
import numpy as np
import joblib

SEQUENCE_LENGTH = 5

df = pd.read_csv("dataset/behavior_processed.csv")

# Sort by user so each user's samples stay together
df = df.sort_values("user")

X = []
y = []

feature_columns = [col for col in df.columns if col != "user"]

for user_id in df["user"].unique():

    user_df = df[df["user"] == user_id]

    features = user_df[feature_columns].values

    # Sliding window
    for i in range(len(features) - SEQUENCE_LENGTH + 1):

        sequence = features[i:i + SEQUENCE_LENGTH]

        X.append(sequence)

        y.append(user_id)

X = np.array(X)
y = np.array(y)

print("Sequence Shape:", X.shape)
print("Label Shape:", y.shape)

np.save("dataset/X_sequences.npy", X)
np.save("dataset/y_labels.npy", y)

print("\n Saved X_sequences.npy")
print(" Saved y_labels.npy")