from personal_account import PersonalAccount

def main():
    # Create an instance of PersonalAccount
    account_number = int(input("Enter account number: "))
    account_holder = input("Enter account holder name: ")
    account = PersonalAccount(account_number, account_holder)

    while True:
        print("\n1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Print transaction history")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            print(f"Deposited {amount} successfully.")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            try:
                account.withdraw(amount)
                print(f"Withdrew {amount} successfully.")
            except ValueError as e:
                print(e)
        elif choice == '3':
            print("Current Balance:", account.get_balance())
        elif choice == '4':
            account.print_transaction_history()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()