from datetime import datetime

def log(msg):
    print(f"[{datetime.utcnow().isoformat()}] {msg}")
