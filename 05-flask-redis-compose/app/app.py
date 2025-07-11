from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

@app.route("/")
def home():
    try:
        r.incr("hits")
        count = r.get("hits").decode("utf-8")
    except redis.exceptions.ConnectionError:
        count = "Redis not available"

    return f"""
    <html>
    <head>
        <title>Flask + Redis</title>
        <style>
            body {{
                background-color: #0f172a;
                color: #e2e8f0;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }}
            h1 {{ font-size: 3rem; color: #38bdf8; }}
            p {{ font-size: 1.2rem; color: #94a3b8; }}
        </style>
    </head>
    <body>
        <h1>🔁 Hit Counter</h1>
        <p>This page has been viewed <strong>{count}</strong> times.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
