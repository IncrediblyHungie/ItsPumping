from api.coins import get_recent_mints
from db.database import coin_exists, insert_immutable
from utils.logger import log

def update_new_coins(conn):
    coins = get_recent_mints()
    for coin in coins:
        mint = coin.get("mint")
        if not mint:
            continue
        if not coin_exists(conn, mint):
            insert_immutable(conn, coin)
            log(f"New coin added: {coin.get('symbol')} ({mint})")
