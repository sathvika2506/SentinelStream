from inference.behavior_predictor import predict_behavior
from utils.risk_aggregator import calculate_final_risk

import numpy as np

# Demo transaction score
transaction_score = 0.72

# Demo behavior sequence
X = np.load("dataset/X_sequences.npy")

behavior = predict_behavior(X[0])

result = calculate_final_risk(
    transaction_score=transaction_score,
    behavior_confidence=behavior["confidence"]
)

print("\n========== SENTINELSTREAM ==========\n")

print("Behavior Prediction")
print(behavior)

print("\nFinal Risk")
print(result)