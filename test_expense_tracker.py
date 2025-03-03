import pytest
from transaction import add_transaction, transactions
from balance import calculate_balance

def test_add_transaction():
    add_transaction("Test Income", 1000, "income")
    assert len(transactions) == 1
    assert transactions[0] == {"name": "Test Income", "amount": 1000, "type": "income"}

def test_calculate_balance():
    transactions.clear()  # Clear existing transactions for testing
    add_transaction("Test Income", 1000, "income")
    add_transaction("Test Expense", 300, "expense")
    assert calculate_balance() == 700  # 1000 - 300 = 700
