# balance.py

from transaction import transactions

def calculate_balance():
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    return total_income - total_expense
