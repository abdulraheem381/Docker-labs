# 🐍 Project 01 – Flask Hello World (Dockerized)

This is a minimal **Flask web application** containerized using **Docker**. It returns a simple "Hello from Flask in Docker!" message when accessed.

---

## 📦 Tech Stack

- Python
- Flask
- Docker

---

## 📁 Folder Structure


01-flask-hello-world/
├── app.py
├── requirements.txt
└── Dockerfile

---


---


---

## 🚀 How to Run the Project

Follow the steps below to build and run the container locally:

```bash
# Step 1: Clone the repository
git clone https://github.com/YOUR_USERNAME/docker-labs-abdul.git
cd docker-labs-abdul/01-flask-hello-world

# Step 2: Build the Docker image
docker build -t flask-hello .

# Step 3: Run the Docker container
docker run -p 5000:5000 flask-hello

✅ Access the Application
Once the container is running, open your browser and visit:

👉 http://localhost:5000

You should see the following output:

Hello from Flask in Docker!

---
🎯 Learning Outcomes
Understanding the structure of a basic Flask web app

Writing a clean and functional Dockerfile

Building and tagging custom Docker images

Exposing container ports to the host machine
