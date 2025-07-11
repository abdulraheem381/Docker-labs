

```markdown
# 🗃️ Project 04 – MySQL Container with Preloaded DB (Dockerized)

This project demonstrates how to run a **MySQL database container** that automatically loads a custom `.sql` script at startup using Docker Compose.  
This setup is perfect for quickly provisioning dev/test databases in CI/CD pipelines or local environments.

---

## 📦 Tech Stack

- MySQL 8.3 (Official Docker Image)
- Docker Compose
- SQL Script for DB seed

---

## 📁 Folder Structure

```

04-custom-mysql-container/
├── init.sql               # SQL script that auto-runs at container start
└── docker-compose.yml     # Defines MySQL container config

````

---

## 🚀 Getting Started

### 1️⃣ Start the MySQL Container

```bash
cd Docker-labs/04-custom-mysql-container
docker-compose up -d
````

This will:

* Start a container named `mysql_preload`
* Create a database `docker_lab`
* Load the SQL schema and seed data from `init.sql`

---

### 2️⃣ Access the Database

```bash
docker exec -it mysql_preload mysql -u root -p
# Enter: rootpass
```

Then inside the MySQL shell:

```sql
USE docker_lab;
SELECT * FROM users;
```

Expected output:

```
+----+--------------+--------------------+
| id | name         | email              |
+----+--------------+--------------------+
|  1 | Abdul Raheem | abdul@example.com  |
|  2 | Jane Doe     | jane@example.com   |
+----+--------------+--------------------+
```

---

## 📌 Environment Variables

Defined in `docker-compose.yml`:

| Variable              | Value       | Description               |
| --------------------- | ----------- | ------------------------- |
| MYSQL\_ROOT\_PASSWORD | rootpass    | Root user password        |
| MYSQL\_DATABASE       | devops\_lab | Database created at start |

---

## 🎯 What You’ll Learn

* How to preload a MySQL DB using Docker volumes
* How to define services with `docker-compose.yml`
* How to persist data and seed databases in containers

---

## 💡 Use Cases

* Dev/Test DB environments
* CI pipelines with test fixtures
* Local DB containers for developers

---



## 📜 License

This project is licensed under the **MIT License**.

```

