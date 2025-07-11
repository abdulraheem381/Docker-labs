import React from 'react';

function App() {
  return (
    <div style={{
      textAlign: "center",
      paddingTop: "100px",
      backgroundColor: "#0f172a",
      height: "100vh",
      color: "#e2e8f0"
    }}>
      <h1 style={{ fontSize: "3rem", color: "#38bdf8" }}>⚛️ React + NGINX</h1>
      <p style={{ fontSize: "1.2rem", color: "#94a3b8" }}>
        This React app is built using Docker and served via NGINX.
      </p>
    </div>
  );
}

export default App;
