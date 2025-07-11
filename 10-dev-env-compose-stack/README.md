
# 🧩 Project 10 – Full Dev Environment with Docker Compose (Flask + PostgreSQL + Adminer)

This project simulates a **complete local development environment** using Docker Compose.  
It includes:
- A Flask API (Python backend)
- A PostgreSQL database
- Adminer (web-based DB GUI)

This is a real-world setup for local dev, microservice testing, or full-stack CI/CD pipelines.

---

## 📦 Tech Stack

- Python 3.11 (Flask)
- PostgreSQL 15 (Alpine)
- Adminer (Database UI)
- Docker Compose

---

## 📁 Folder Structure

```

10-dev-env-compose-stack/
├── app/
│   ├── app.py              # Flask backend API
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Flask container image
└── docker-compose.yml      # Compose config for full stack

````

---

## 🚀 Getting Started

### 1️⃣ Run the Full Stack

```bash
cd Docker-labs/10-dev-env-compose-stack
docker compose up --build
````

This will:

* Build and start the Flask API
* Start PostgreSQL database with preconfigured user + DB
* Launch Adminer for visual DB management

---

## 🌍 Access Your Services

| Service   | URL                                                                 |
| --------- | ------------------------------------------------------------------- |
| Flask API | [http://localhost:5000](http://localhost:5000)                      |
| Adminer   | [http://localhost:8080](http://localhost:8080) (or 8181 if changed) |

> 🔐 **Adminer Credentials**:
>
> * Server: `db`
> * Username: `postgres`
> * Password: `password`
> * Database: `devopsdb`

---

## ✅ Expected Output (Flask API)

```
✅ Connected to PostgreSQL
DB Version: PostgreSQL 15.x on Alpine
```

If the database is unavailable, it will show:

```
❌ Database Connection Failed
```

---

## 🧠 What You’ll Learn

* Building production-ready dev environments with Docker Compose
* Connecting microservices (Flask ↔ PostgreSQL) using service names
* Managing databases with Adminer in local setups
* Handling environment variables for DB config

---

## 💡 Use Cases

* Local dev for full-stack applications
* Backend testing environments
* CI/CD mock stacks with real services

---

## 🛠 Environment Variables

| Key                | Value    |
| ------------------ | -------- |
| POSTGRES\_DB       | devopsdb |
| POSTGRES\_USER     | postgres |
| POSTGRES\_PASSWORD | password |
| POSTGRES\_HOST     | db       |
