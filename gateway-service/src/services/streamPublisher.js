const { client } = require("../config/redis");

async function publishTransaction(transaction) {
    await client.xAdd(
        "fraud-stream",
        "*",
        {
            data: JSON.stringify(transaction)
        }
    );

    console.log("📨 Published to fraud-stream");
}

module.exports = {
    publishTransaction
};