from db.database import insert_mutable
from api.coins import fetch_coin_details
from datetime import datetime
from utils.logger import log

def update_all_stats(conn):
    cur = conn.cursor()
    cur.execute("SELECT mint FROM coins")
    mints = [row[0] for row in cur.fetchall()]
    now = datetime.utcnow().isoformat()

    for mint in mints:
        details = fetch_coin_details(mint)
        if details:
            insert_mutable(conn, mint, details, now)
            log(f"Updated stats: {details.get('symbol')} - {details.get('market_cap')} SOL")
