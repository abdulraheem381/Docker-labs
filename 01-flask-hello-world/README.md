project:
  id: 01
  name: Flask Hello World
  path: 01-flask-hello-world
  description: A minimal Flask web application containerized with Docker.
  level: beginner
  tech_stack:
    - Python
    - Flask
    - Docker
  structure:
    - app.py
    - requirements.txt
    - Dockerfile
  steps:
    - step: Clone the repository or download this folder
      command: |
        git clone https://github.com/YOUR_USERNAME/docker-labs-abdul.git
        cd docker-labs-abdul/01-flask-hello-world
    - step: Build the Docker image
      command: docker build -t flask-hello .
    - step: Run the Docker container
      command: docker run -p 5000:5000 flask-hello
    - step: Test the application
      url: http://localhost:5000
      expected_output: Hello from Flask in Docker!
  learnings:
    - How to write a simple Dockerfile
    - How to containerize a Python app
    - How to expose and bind ports
    - How to build and run images using the Docker CLI
  author:
    name: Abdul Raheem
    role: DevOps Engineer
    
  license: MIT
