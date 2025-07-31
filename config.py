# ---------------------------------------
# 📡 API Endpoints
# ---------------------------------------

NEW_COINS_URL = (
    "https://frontend-api-v3.pump.fun/coins?"
    "offset=0&limit=48&sort=created_timestamp&includeNsfw=false&order=DESC"
)

COIN_DETAILS_URL = "https://frontend-api-v3.pump.fun/coins/{mint}"
TOP_HOLDERS_URL = "https://frontend-api-v3.pump.fun/coins/top-holders/{mint}"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# ---------------------------------------
# 🛢️ MySQL Database Configuration
# ---------------------------------------

MYSQL_CONFIG = {
    "host": "localhost",
    "user": "pumpfun",
    "password": "RUNTHATSHITIHATEMYJOB!!!",
    "database": "pumpfun",
    "port": 3306,
    # use the pure Python implementation for stability when multiple
    # connections are active concurrently
    "use_pure": True
}

# ---------------------------------------
# 🔁 Task Polling Intervals (seconds)
# ---------------------------------------

WORKERS = {
    "update_new_coins": {
        "enabled": True,
        "interval": 10  # how often to poll new mints
    },
    "update_coin_stats": {
        "enabled": True,
        "interval": 5   # how often to update market cap / price
    },
    "update_top_holders": {
        "enabled": True,
        "interval": 60  # update holder info every minute
    },
    # future: "execute_trading": {"enabled": True, "interval": 60}
}
