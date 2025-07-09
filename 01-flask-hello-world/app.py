from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <title>Flask in Docker</title>
        <style>
          body {
            background-color: #0f172a;
            color: #e2e8f0;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 100px;
          }
          h1 {
            font-size: 3rem;
            margin-bottom: 20px;
            color: #38bdf8;
          }
          p {
            font-size: 1.2rem;
            color: #94a3b8;
          }
        </style>
      </head>
      <body>
        <h1>Hello from Flask in Docker! 🐳</h1>
        <p>This app is running inside a container, served by Flask, and exposed on port 5000.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
