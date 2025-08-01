import mysql.connector
from config import MYSQL_CONFIG
from models.fields import IMMUTABLE_FIELDS, MUTABLE_FIELDS

def get_conn():
    return mysql.connector.connect(**MYSQL_CONFIG)

def setup_database(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coins (
            mint VARCHAR(100) PRIMARY KEY,
            name VARCHAR(255),
            symbol VARCHAR(50),
            description TEXT,
            image_uri TEXT,
            metadata_uri TEXT,
            twitter TEXT,
            telegram TEXT,
            website TEXT,
            creator TEXT,
            bonding_curve TEXT,
            associated_bonding_curve TEXT,
            created_timestamp BIGINT,
            total_supply BIGINT,
            show_name BOOLEAN,
            nsfw BOOLEAN,
            is_currently_live BOOLEAN,
            complete BOOLEAN
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coin_stats (
            id INT AUTO_INCREMENT PRIMARY KEY,
            mint VARCHAR(100),
            timestamp DATETIME,
            market_cap DOUBLE,
            usd_market_cap DOUBLE,
            virtual_sol_reserves BIGINT,
            virtual_token_reserves BIGINT,
            last_trade_timestamp BIGINT,
            FOREIGN KEY (mint) REFERENCES coins(mint)
        )
    """)

    conn.commit()
    cursor.close()

def coin_exists(conn, mint):
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM coins WHERE mint = %s", (mint,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None

def insert_immutable(conn, coin):
    data = {k: coin.get(k) for k in IMMUTABLE_FIELDS}
    placeholders = ', '.join(['%s'] * len(data))
    columns = ', '.join(data.keys())
    sql = f"INSERT IGNORE INTO coins ({columns}) VALUES ({placeholders})"
    cursor = conn.cursor()
    cursor.execute(sql, list(data.values()))
    conn.commit()
    cursor.close()

def insert_mutable(conn, mint, details, timestamp):
    values = [mint, timestamp] + [details.get(k) for k in MUTABLE_FIELDS]
    sql = """
        INSERT INTO coin_stats (
            mint, timestamp, market_cap, usd_market_cap,
            virtual_sol_reserves, virtual_token_reserves, last_trade_timestamp
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
