def calculate_final_risk(
    transaction_score,
    behavior_confidence
):

    behavior_risk = 1 - behavior_confidence

    final_score = (
        (0.6 * transaction_score)
        +
        (0.4 * behavior_risk)
    )

    return {
        "transactionRisk": round(transaction_score,3),
        "behaviorConfidence": round(behavior_confidence,3),
        "behaviorRisk": round(behavior_risk,3),
        "finalRisk": round(final_score,3)
    }