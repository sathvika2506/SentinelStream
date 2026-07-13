import numpy as np
from tensorflow.keras.models import load_model

# Load model once
model = load_model("models/behavior_lstm.keras")


def predict_behavior(sequence):

    sequence = np.array(sequence)

    sequence = sequence.reshape(1, 5, 13)

    prediction = model.predict(sequence, verbose=0)

    confidence = float(np.max(prediction))

    predicted_user = int(np.argmax(prediction))

    return {
        "predicted_user": predicted_user,
        "confidence": confidence,
    }