# Pump.fun Tracker

Modular data ingestion, coin monitoring, and trading logic for Pump.fun.

## Features

- Automatically installs dependencies. If MySQL is missing, the startup
  script runs `sudo apt install -y mysql-server` after an `apt-get update`.
- Records the starting market cap for each newly discovered token.
- Each worker opens and closes its own MySQL connection every cycle, so you
  can safely run queries in parallel without interrupting the tracker.
- Uses the pure Python MySQL driver (`use_pure=True`) for stability when
  multiple connections are active.
