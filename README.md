# SentinelStream

A distributed fraud detection platform that combines transaction analysis and behavioral biometrics to detect suspicious financial activity in real time.

SentinelStream uses an event-driven architecture where transaction requests are streamed through Redis Streams to a Python ML service that evaluates both transaction risk and user behavioral patterns before producing a final fraud score.

---

## Architecture

```
                    Client
                       │
                       ▼
              Express Gateway
                       │
                       ▼
                 Redis Streams
                       │
                       ▼
                 Python Worker
                /             \
               /               \
      Transaction Engine   Behavior Engine
       (ML Models)          (LSTM Model)
               \               /
                \             /
                 ▼           ▼
                 Risk Aggregator
                       │
                       ▼
                  PostgreSQL
```

---

## Features

- Distributed event-driven architecture using Redis Streams
- REST API built with Express.js
- Transaction fraud detection using Machine Learning
- Behavioral biometric authentication using LSTM
- Centralized risk aggregation pipeline
- gRPC communication between services
- PostgreSQL integration
- Modular microservice-inspired design

---

## Tech Stack

### Backend
- Node.js
- Express.js
- PostgreSQL
- Redis Streams
- gRPC

### Machine Learning
- Python
- TensorFlow / Keras
- Scikit-learn
- XGBoost
- NumPy
- Pandas

---

## Machine Learning Pipeline

### Transaction Engine

- Data preprocessing
- Feature engineering
- Logistic Regression baseline
- XGBoost fraud classifier

### Behavior Engine

User interaction features are transformed into temporal sequences and processed using an LSTM network.

Behavioral signals include:

- Typing speed
- Error rate
- Dwell time
- Flight time
- Scroll behaviour
- Swipe speed
- Touch pressure
- Double click frequency
- Device orientation

The model estimates behavioral confidence, which is combined with transaction risk to generate a final fraud score.

---

## Project Structure

```
SentinelStream

gateway-service/
    Express API
    Redis Publisher

ml-service/
    Transaction ML
    Behaviour Engine
    gRPC Server

shared/
    Protocol Buffers

docs/
    Architecture
    API Documentation
```

---

## Workflow

1. Client submits a transaction.
2. Express Gateway validates the request.
3. Transaction is published to Redis Streams.
4. Python worker consumes the event.
5. Transaction model predicts fraud probability.
6. Behavioral engine analyzes user interaction sequences.
7. Risk Aggregator combines both signals.
8. Final fraud score is returned.

---

## Future Improvements

- Real-time Kafka pipeline
- Transformer-based behavioral model
- Device fingerprinting
- Online model retraining
- Explainable AI dashboard
- Model monitoring and drift detection

---

## Installation

### Clone

```bash
git clone https://github.com/sathvika2506/SentinelStream.git
```

### Install Gateway

```bash
cd gateway-service
npm install
```

### Install ML Service

```bash
cd ml-service
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file using `.env.example`.

Example:

```
DATABASE_URL=

REDIS_URL=

PORT=5000

GROQ_API_KEY=
```

---

## Status

Current Version: **v1.0**

- Transaction Risk Engine
- Behavioral Biometrics Engine
- LSTM-based Sequence Classification
- Distributed Processing Pipeline
- Risk Aggregation
