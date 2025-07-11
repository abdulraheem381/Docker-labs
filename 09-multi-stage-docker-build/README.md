
# 🧱 Project 09 – Multi-Stage Docker Build (Node.js Optimized)

This project demonstrates how to build a **production-ready Node.js application** using a **multi-stage Docker build**.  
It separates the build stage from the runtime stage to produce a clean, lightweight final image.

---

## 📦 Tech Stack

- Node.js (Alpine image)
- Express.js
- Docker (Multi-stage build)

---

## 📁 Folder Structure

```

09-multi-stage-docker-build/
├── Dockerfile            # Multi-stage build instructions
└── src/
├── index.js          # Express web server
└── package.json      # App dependencies

````

---

## 🚀 Getting Started

### 1️⃣ Build the Docker Image

```bash
cd Docker-labs/09-multi-stage-docker-build
docker build -t node-prod-app .
````

### 2️⃣ Run the Container

```bash
docker run -p 8080:8080 node-prod-app
```

---

## 🌍 Access the App

Open your browser:
👉 **[http://localhost:8080](http://localhost:8080)**

Expected output:

> “🚀 Optimized Node.js App from Multi-Stage Docker Build”

---

## ⚙️ Multi-Stage Explained

| Stage       | Image            | Purpose                                 |
| ----------- | ---------------- | --------------------------------------- |
| **Builder** | `node:20-alpine` | Installs dependencies, builds app       |
| **Runtime** | `node:20-alpine` | Runs only the final app, no build tools |

> ✅ Final image size: **\~90 MB**, compared to 500–800 MB if you don't optimize.

---

## 🎯 What You’ll Learn

* How multi-stage builds reduce image bloat
* Clean separation of build vs. deploy environments
* Efficient Docker layering and caching

---

## 💡 Use Cases

* Production backend deployment
* CI/CD pipelines with small deployable images
* Security-focused container builds

