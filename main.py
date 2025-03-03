from transaction import add_transaction, transactions
from balance import calculate_balance
from display import display_transactions
from file_operations import load_from_file, save_to_file

def main():
    load_from_file('transactions.txt')
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Transaction")
        print("2. Display Transactions")
        print("3. Calculate Balance")
        print("4. Save Transactions")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            name = input("Enter transaction name: ")
            amount = float(input("Enter transaction amount: "))
            transaction_type = input("Enter transaction type (income/expense): ").lower()
            if transaction_type in ['income', 'expense']:
                add_transaction(name, amount, transaction_type)
            else:
                print("Invalid transaction type. Please enter 'income' or 'expense'.")
        
        elif choice == '2':
            display_transactions()
        
        elif choice == '3':
            print(f"Net Balance: ${calculate_balance():.2f}")
        
        elif choice == '4':
            save_to_file('transactions.txt')
        
        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
