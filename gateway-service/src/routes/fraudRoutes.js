const express = require("express");
const router = express.Router();
const { analyzeTransaction } = require("../controllers/fraudController");

router.post("/analyze", analyzeTransaction);

module.exports = router;