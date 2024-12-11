#!/usr/bin/env bash

# Start the SSH server in the background
/usr/sbin/sshd -D

echo "Initializing Airflow database..."
if ! airflow db init; then
    echo "Error initializing Airflow database"
    exit 1
fi

echo "Airflow webserver starting..."
if ! airflow webserver; then
    echo "Error starting Airflow webserver"
    exit 1
fi

echo "Airflow scheduler starting..."
if ! airflow scheduler; then
    echo "Error starting Airflow scheduler"
    exit 1
fi

