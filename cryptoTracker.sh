#!/bin/bash

echo "Crypto Tracker Menu"
echo "1. Update cryptocurrency data"
echo "2. Export cryptocurrency data to CSV/JSON/Excel"
echo "3. Exit"
read -p "Choose an option: " option

case $option in
    1)
        echo "Updating cryptocurrency data..."
        "C:/Program Files/Spyder/Python/python.exe" cryptoTracker.py
        echo "Update completed."
        ;;
    2)
        echo "Exporting cryptocurrency data..."
        python3 cryptoTracker.py export  # or use the full path if needed
        ;;
    3)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option!"
        ;;
esac
