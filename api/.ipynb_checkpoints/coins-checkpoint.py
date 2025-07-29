import requests
from config import NEW_COINS_URL, COIN_DETAILS_URL, HEADERS

def get_recent_mints():
    resp = requests.get(NEW_COINS_URL, headers=HEADERS)
    if resp.ok:
        return resp.json()
    return []

def fetch_coin_details(mint):
    url = COIN_DETAILS_URL.format(mint=mint)
    resp = requests.get(url, headers=HEADERS)
    if resp.ok:
        return resp.json()
    return None
