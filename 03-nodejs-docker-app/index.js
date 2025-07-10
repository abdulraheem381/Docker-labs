const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Node.js in Docker</title>
      <style>
        body {
          background: linear-gradient(135deg, #0f172a, #1e293b);
          color: #e2e8f0;
          font-family: 'Segoe UI', sans-serif;
          text-align: center;
          padding-top: 100px;
        }
        h1 {
          font-size: 3rem;
          color: #38bdf8;
        }
        p {
          font-size: 1.2rem;
          color: #94a3b8;
        }
        .badge {
          margin-top: 2rem;
          display: inline-block;
          padding: 0.5rem 1rem;
          border-radius: 999px;
          background-color: #1e40af;
          color: white;
          font-size: 0.9rem;
          box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
        }
      </style>
    </head>
    <body>
      <h1>🚀 Node.js App Running in Docker</h1>
      <p>This is a simple Express.js application containerized using Docker.</p>
      <div class="badge">Docker-labs • Project 03</div>
    </body>
    </html>
  `);
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`✅ Server is running at http://localhost:${PORT}`);
});
