import os
import pandas as pd

folder = "dataset"

dfs = []

for file in os.listdir(folder):
    if file.endswith(".xlsx"):
        path = os.path.join(folder, file)

        df = pd.read_excel(path)

        dfs.append(df)

merged = pd.concat(dfs, ignore_index=True)

print("Merged Shape:", merged.shape)

print("\nUnique Users:")
print(merged["user"].unique())

merged.to_csv("dataset/behavior_dataset.csv", index=False)

print("\n Saved behavior_dataset.csv")