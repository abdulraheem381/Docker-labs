
# 🔄 Project 05 – Flask + Redis (Docker Compose)

This project demonstrates how to run a **multi-container app** using Docker Compose.  
A simple Flask application connects to a Redis container to count the number of times the page is refreshed — a classic "hit counter" app.

---

## 📦 Tech Stack

- Python 3.11 (Flask)
- Redis (Alpine image)
- Docker Compose

---

## 📁 Folder Structure

```

05-flask-redis-compose/
├── app/
│   ├── app.py             # Flask application (hit counter)
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Flask container image
└── docker-compose.yml     # Runs Flask + Redis together

````

---

## 🚀 Getting Started

### 1️⃣ Run the App with Compose

```bash
cd Docker-labs/05-flask-redis-compose
docker-compose up --build
````

This will:

* Build the Flask app image
* Pull the Redis image
* Create a network and start both services

---

## 🌍 Access the App

Open your browser and go to:
👉 [http://localhost:5000](http://localhost:5000)

You’ll see a dark-themed UI that displays the **number of times the page has been refreshed** (stored in Redis):

> “This page has been viewed **X** times.”

---

## 🎯 What You’ll Learn

* Creating multi-container environments using Docker Compose
* Flask to Redis communication via environment variables
* Networking between services in Compose
* Persisting state with an in-memory database (Redis)

---

## 💡 Use Cases

* Dev/testing microservices locally
* Caching page views or sessions
* Building stateful backend environments for CI/CD demos

---
