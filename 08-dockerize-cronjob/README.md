
# ⏱️ Project 08 – Cron Job in Docker

This project demonstrates how to run a **cron job inside a Docker container** using Alpine Linux and `crond`.  
A shell script runs every minute and appends a timestamp to a log file.

---

## 📦 Tech Stack

- Alpine Linux
- Cron (cronie)
- Bash shell script
- Docker

---

## 📁 Folder Structure

```

08-dockerize-cronjob/
├── task.sh             # Script executed by cron every minute
├── crontab.txt         # Cron schedule definition
└── Dockerfile          # Container configuration

````

---

## 🚀 Getting Started

### 1️⃣ Build the Docker Image

```bash
cd Docker-labs/08-dockerize-cronjob
docker build -t cron-job-app .
````

### 2️⃣ Run the Container

```bash
docker run -d --name cronjob cron-job-app
```

---

## 📋 View Cron Output

After 2–3 minutes, check the logs:

```bash
docker exec -it cronjob cat /var/log/cron.log
```

Expected output:

```
📅 Cron job executed at: 2025-07-10 14:00:01
📅 Cron job executed at: 2025-07-10 14:01:01
📅 Cron job executed at: 2025-07-10 14:02:01
```

---

## 🧠 What You’ll Learn

* How to configure cron inside a Docker container
* How to run background jobs in containers
* How to use Alpine + cronie for lightweight task automation

---

## 💡 Use Cases

* Scheduled data syncs
* Backup or cleanup jobs
* Periodic monitoring/log collection

---

## ⚙️ Cron Schedule Used

| Field       | Value        | Meaning                      |
| ----------- | ------------ | ---------------------------- |
| `* * * * *` | Every minute | (min hour day month weekday) |

You can modify `crontab.txt` to change the frequency.

