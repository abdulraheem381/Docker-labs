
# 🐍 Project 07 – Alpine Minimal Python App (Dockerized)

This project demonstrates how to build a **lightweight Python application** using the `python:alpine` image.  
It runs a simple script to display the current time inside a highly optimized, minimal Docker container.

---

## 📦 Tech Stack

- Python 3.11
- Alpine Linux (base image)
- Docker (optimized build)

---

## 📁 Folder Structure

```

07-alpine-minimal-python/
├── main.py           # Minimal Python script
└── Dockerfile        # Alpine-based container config

````

---

## 🚀 Getting Started

### 1️⃣ Build the Docker Image

```bash
cd Docker-labs/07-alpine-minimal-python
docker build -t alpine-python-app .
````

### 2️⃣ Run the Container

```bash
docker run alpine-python-app
```

---

## ✅ Output Example

```
🔹 Minimal Python App Running in Docker
🕒 Current Time: 2025-07-10 12:34:56
```

> Output time updates every time you run the container.

---

## 🎯 What You’ll Learn

* How to use `python:alpine` for small image builds
* How to build CLI-style containers
* Image optimization and size reduction

---

## 📊 Image Size Comparison

| Base Image           | Approx. Size |
| -------------------- | ------------ |
| `python:3.11`        | \~800 MB     |
| `python:3.11-alpine` | \~55 MB      |

> Using Alpine reduces image size by over 90%.

---

## 💡 Use Cases

* CLI tools in Docker
* Lightweight jobs or cron tasks
* Microservices with small footprint

