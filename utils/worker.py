import threading
import time
from utils.logger import log
from db.database import get_conn

def start_worker(name, interval, target):
    def loop():
        conn = get_conn()
        log(f"Worker '{name}' started with interval {interval}s using dedicated connection.")
        while True:
            try:
                target(conn)
            except Exception as e:
                log(f"[ERROR] Worker '{name}' failed: {e}")
                try:
                    conn.close()
                except Exception:
                    pass
                conn = get_conn()
            time.sleep(interval)
    t = threading.Thread(target=loop, daemon=True)
    t.start()
    return t
