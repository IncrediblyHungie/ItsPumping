from api.holders import fetch_top_holders
from db.database import insert_top_holder
from datetime import datetime
from utils.logger import log


def update_top_holders(conn):
    cur = conn.cursor()
    cur.execute("SELECT mint FROM coins")
    mints = [row[0] for row in cur.fetchall()]
    cur.close()

    now = datetime.utcnow().isoformat()
    for mint in mints:
        holders = fetch_top_holders(mint)
        for h in holders:
            insert_top_holder(conn, mint, h, now)
        if holders:
            log(f"Updated holders for {mint}")

