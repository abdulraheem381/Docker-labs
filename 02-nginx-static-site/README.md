# 🌐 Project 02 – NGINX Static Site (Dockerized)

A fully containerized static HTML website served using the official **NGINX Docker image**.  
This project demonstrates how to deploy a personal landing page or simple "Under Construction" site using Docker.

---

## 📦 Tech Stack

- HTML + CSS
- NGINX (Alpine base image)
- Docker

---


---

## 🚀 Getting Started

### 1️⃣ Build the Docker Image

```bash
cd Docker-labs/02-nginx-static-site
docker build -t nginx-static .

docker run -p 80:80 nginx-static



🌍 Access the Site
Open your browser and visit:
👉 http://localhost:80

You’ll see a modern dark-themed HTML page that says:

“🚀 Deployed with Docker + NGINX”


