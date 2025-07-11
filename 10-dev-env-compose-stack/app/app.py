from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("POSTGRES_HOST", "db"),
            dbname="devopsdb",
            user="postgres",
            password="password"
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return f"<h1>✅ Connected to PostgreSQL</h1><p>DB Version: {version}</p>"
    except Exception as e:
        return f"<h1>❌ Database Connection Failed</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
