from api.coins import get_recent_mints, fetch_coin_details
from db.database import coin_exists, insert_immutable
from utils.logger import log

def update_new_coins(conn):
    coins = get_recent_mints()
    for coin in coins:
        mint = coin.get("mint")
        if not mint:
            continue
        if not coin_exists(conn, mint):
            details = fetch_coin_details(mint)
            if details and details.get("market_cap") is not None:
                coin["starting_market_cap"] = details.get("market_cap")
            insert_immutable(conn, coin)
            log(
                f"New coin added: {coin.get('symbol')} ({mint})"
                + (
                    f" starting market cap {coin.get('starting_market_cap')}" if coin.get('starting_market_cap') is not None else ""
                )
            )
