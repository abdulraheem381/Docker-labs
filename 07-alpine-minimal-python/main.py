from datetime import datetime

def greet():
    print("🔹 Minimal Python App Running in Docker")
    print(f"🕒 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    greet()
