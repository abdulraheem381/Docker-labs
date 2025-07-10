project:
  id: 02
  name: NGINX Static Site
  path: 02-nginx-static-site
  description: |
    A fully containerized static HTML website served using the official NGINX image and Docker.
    Demonstrates how to deploy a static landing page inside a containerized web server.
  level: beginner

tech_stack:
  - HTML
  - CSS
  - NGINX (alpine)
  - Docker

structure:
  - index.html  # The static website page
  - Dockerfile  # Image build instructions

instructions:
  steps:
    - step: Navigate to the project folder
      command: cd docker-labs-abdul/02-nginx-static-site

    - step: Build the Docker image
      command: docker build -t nginx-static .

    - step: Run the Docker container
      command: docker run -p 80:80 nginx-static

  output_url: http://localhost:80
  expected_result: |
    Displays a modern, styled HTML landing page with a dark theme.
    Includes a heading "🚀 Deployed with Docker + NGINX" and a brief message.

learnings:
  - Using official NGINX image to serve static files
  - Writing a Dockerfile to copy HTML into containers
  - Port mapping using docker run
  - Minimal production-ready static deployments

use_cases:
  - Personal landing pages
  - Under construction pages
  - Static UI demos


license: MIT
