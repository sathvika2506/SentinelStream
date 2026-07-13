const { v4: uuidv4 } = require("uuid");
const pool = require("../config/db");
const { publishTransaction } = require("../services/streamPublisher");

const analyzeTransaction = async (req, res) => {
  try {
    const {
      userId,
      amount,
      merchant,
      country,
      device,
      hour
    } = req.body;

    const transactionId = uuidv4();

    await pool.query(
      `
            INSERT INTO transactions
            (id, user_id, amount, merchant, country, device, hour)
            VALUES ($1,$2,$3,$4,$5,$6,$7)
            `,
      [
        transactionId,
        userId,
        amount,
        merchant,
        country,
        device,
        hour
      ]
    );
    await publishTransaction({
      transactionId,
      userId,
      amount,
      merchant,
      country,
      device,
      hour
    });

    res.status(202).json({
      success: true,
      transactionId,
      message: "Transaction queued for analysis."
    });

  } catch (err) {
    console.error(err);

    res.status(500).json({
      success: false,
      message: "Internal Server Error"
    });
  }
};

module.exports = {
  analyzeTransaction
};