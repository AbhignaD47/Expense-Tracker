# transaction.py

transactions = []

def add_transaction(name, amount, transaction_type):
    transaction = {
        "name": name,
        "amount": amount,
        "type": transaction_type
    }
    transactions.append(transaction)
    print(f"Transaction added: {transaction}")
