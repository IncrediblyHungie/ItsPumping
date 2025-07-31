import threading
import time
from utils.logger import log
from db.database import get_conn

def start_worker(name, interval, target):
    def loop():
        log(f"Worker '{name}' started with interval {interval}s.")
        while True:
            conn = get_conn()
            try:
                target(conn)
            except Exception as e:
                log(f"[ERROR] Worker '{name}' failed: {e}")
            finally:
                try:
                    conn.close()
                except Exception:
                    pass
            time.sleep(interval)
    t = threading.Thread(target=loop, daemon=True)
    t.start()
    return t
