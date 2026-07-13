const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");
const helmet = require("helmet");
const morgan = require("morgan"); 
const fraudRoutes = require("./routes/fraudRoutes"); 
const { connectRedis } = require("./config/redis");

dotenv.config();

const app = express();

app.use(express.json());
app.use(cors());
app.use(helmet());
app.use(morgan("dev")); 
app.use("/api/v1/fraud", fraudRoutes);

app.get("/", (req, res) => {
    res.json({
        service: "SentinelStream Gateway",
        status: "Running",
        version: "1.0.0"
    });
});

const PORT = process.env.PORT || 5000; 
connectRedis();

app.listen(PORT, () => {
    console.log(`Sentinel Gateway running on port ${PORT}`);
});