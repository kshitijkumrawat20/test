const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(cors());

// N8N Webhook URL (Replace this with your actual URL)
const EC2_HTTP_URL =
  "http://ec2-13-58-27-158.us-east-2.compute.amazonaws.com:5678/webhook/0b95a964-2518-4250-929c-0e6f6ba766ab";

// Proxy Route
app.post("/", async (req, res) => {
  try {
    const response = await axios.post(EC2_HTTP_URL, req.body);
    res.json(response.data); // Send back response from N8N
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
