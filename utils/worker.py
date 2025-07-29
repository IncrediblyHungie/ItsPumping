import threading
import time
from utils.logger import log

def start_worker(name, interval, target, conn):
    def loop():
        log(f"Worker '{name}' started with interval {interval}s.")
        while True:
            try:
                target(conn)
            except Exception as e:
                log(f"[ERROR] Worker '{name}' failed: {e}")
            time.sleep(interval)
    t = threading.Thread(target=loop, daemon=True)
    t.start()
    return t
