# ⚙️ Project 03 – Node.js Docker App

This project demonstrates how to containerize a **Node.js Express API** using Docker.  
The application returns a clean, styled HTML response served at `http://localhost:3000`.

---

## 📦 Tech Stack

- Node.js (v20+)
- Express.js
- Docker (alpine image)

---


---

## 🚀 Getting Started

### 1️⃣ Build the Docker Image

```bash
cd Docker-labs/03-nodejs-docker-app
docker build -t node-app .
docker run -p 3000:3000 node-app

🌍 Access the App
Open your browser and go to:
👉 http://localhost:3000

You’ll see a modern, dark-themed landing page with a message:

“🚀 Node.js App Running in Docker”
