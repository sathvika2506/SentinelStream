const pool = require("./config/db");
async function testDB() {
    try {
        const result = await pool.query("SELECT NOW()");
        console.log("✅ PostgreSQL Connected");
        console.log(result.rows[0]);
    } catch (err) {
        console.error(err);
    } finally {
        pool.end();
    }
}

testDB();