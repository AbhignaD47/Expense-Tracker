# file_operations.py

import json
from transaction import transactions

def save_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(transactions, file)
    print(f"Transactions saved to {filename}")

def load_from_file(filename):
    global transactions
    try:
        with open(filename, 'r') as file:
            transactions.clear()  # Clear existing transactions
            transactions.extend(json.load(file))
        print(f"Transactions loaded from {filename}")
    except FileNotFoundError:
        print(f"No previous data found. Starting fresh.")
