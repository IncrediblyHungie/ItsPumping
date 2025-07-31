#!/bin/bash

cd "$(dirname "$0")"

echo "🔄 Updating package lists..."
sudo apt-get update -y

echo "🔄 Setting up virtual environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "✅ Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate
echo "📦 Activated virtual environment."

# Install dependencies
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
  echo "📦 Dependencies installed."
else
  echo "⚠️ No requirements.txt found. Skipping dependency install."
fi

# MySQL check and bootstrap
echo "🔍 Checking MySQL installation..."
if ! command -v mysql &> /dev/null; then
  echo "❌ MySQL is not installed. Installing..."
  sudo apt install -y mysql-server
fi

echo "🧠 Verifying if database and user exist..."

DB_EXISTS=$(mysql -u root -sse "SHOW DATABASES LIKE 'pumpfun';")
if [ "$DB_EXISTS" != "pumpfun" ]; then
  echo "🛠️ Creating database and user..."
  mysql -u root <<EOF
CREATE DATABASE pumpfun;
CREATE USER IF NOT EXISTS 'pumpfun'@'localhost' IDENTIFIED BY 'RUNTHATSHITIHATEMYJOB!!!';
GRANT ALL PRIVILEGES ON pumpfun.* TO 'pumpfun'@'localhost';
FLUSH PRIVILEGES;
EOF
  echo "✅ MySQL database and user created."
else
  echo "✅ Database 'pumpfun' already exists. Skipping creation."
fi

# Launch the tracker
echo "🚀 Starting the Pump.fun tracker..."
PYTHONPATH="$(pwd)" python3 main.py
