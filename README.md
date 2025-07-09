# 🐳 docker-labs

A collection of hands-on Docker mini-projects built by Me. Each lab demonstrates practical use of Docker in modern DevOps workflows.

---

## 📁 Project Index

| # | Project | Description |
|--|---------|-------------|
| 01 | [Flask App](./01-flask-app) | A minimal Python Flask app dockerized for local testing |
| 02 | [NGINX Static Site](./02-nginx-static-site) | Serve a basic static HTML page using NGINX |
| 03 | [Node.js App](./03-nodejs-app) | Node Express app packaged in Docker |
| 04 | [MySQL Init DB](./04-mysql-init-db) | MySQL container preloaded with `.sql` file |
| 05 | [Multi-Container App](./05-multi-container-app) | Flask app + PostgreSQL + Redis via Compose |
| 06 | [React + NGINX](./06-react-nginx) | Serve React static app using NGINX |
| 07 | [Minimal Alpine Image](./07-alpine-minimal) | Docker image built from alpine for size optimization |
| 08 | [Local Dev Environment](./08-local-dev-env) | Full dev stack: Flask + Redis + PostgreSQL + Adminer |

---

## 💡 How to Use

Clone the repo and navigate to any project:

```bash
git clone https://github.com/yourusername/docker-labs.git
cd docker-labs/01-flask-app
docker build -t flask-app .
docker run -p 5000:5000 flask-app
