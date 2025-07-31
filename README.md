# Pump.fun Tracker

Modular data ingestion, coin monitoring, and trading logic for Pump.fun.

## Features

- Automatically installs dependencies. If MySQL is missing, the startup
  script runs `sudo apt install -y mysql-server` after an `apt-get update`.
- Records the starting market cap for each newly discovered token.
- Uses a dedicated MySQL connection for each worker thread to prevent
  "Unread result" errors.
