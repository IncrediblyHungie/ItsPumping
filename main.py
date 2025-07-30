from db.database import get_conn, setup_database
from config import WORKERS
from utils.worker import start_worker
from update import update_new_coins, update_coin_stats
import time

TASK_MAP = {
    "update_new_coins": update_new_coins.update_new_coins,
    "update_coin_stats": update_coin_stats.update_all_stats,
    # "update_top_holders": ...
    # "execute_trading": ...
}

def main():
    conn = get_conn()
    setup_database(conn)
    conn.close()

    for name, config in WORKERS.items():
        if config["enabled"] and name in TASK_MAP:
            start_worker(name, config["interval"], TASK_MAP[name])

    while True:
        time.sleep(60)  # main thread idles while workers run

if __name__ == "__main__":
    main()
