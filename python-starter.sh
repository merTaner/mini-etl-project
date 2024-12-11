#!/bin/bash

# Run ETL scripts
echo "Starting load_to_mariadb.py..."
python /app/scripts/load_to_mariadb.py
sleep 1

echo "Starting transform.py..."
python /app/scripts/transfrom.py
sleep 1

echo "Starting load.py..."
python scripts/load.py

echo "Scripts completed, keeping container alive..."
tail -f /dev/null