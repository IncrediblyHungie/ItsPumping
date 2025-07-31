import requests
from config import TOP_HOLDERS_URL, HEADERS


def fetch_top_holders(mint):
    """Return list of top holder entries for the given mint."""
    url = TOP_HOLDERS_URL.format(mint=mint)
    resp = requests.get(url, headers=HEADERS)
    if not resp.ok:
        return []
    data = resp.json()
    # API may nest holders under "topHolders"->"value" or directly under "value"
    if isinstance(data, dict):
        if "topHolders" in data:
            return data.get("topHolders", {}).get("value", [])
        return data.get("value", [])
    return []

