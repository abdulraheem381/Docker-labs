CREATE DATABASE IF NOT EXISTS docker_lab;

USE devops_lab;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES
('Abdul Raheem', 'abdul@example.com'),
('Jane Doe', 'jane@example.com');
