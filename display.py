# display.py

from transaction import transactions

def display_transactions():
    if not transactions:
        print("No transactions found.")
        return
    print("\nAll Transactions:")
    for t in transactions:
        print(f"{t['type'].capitalize()}: {t['name']} - ${t['amount']:.2f}")
