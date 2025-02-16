# Personal Bank Account Project

This project is a simple implementation of a personal bank account management system. It includes classes for handling transactions and managing account details.

## Project Structure

```
personal-bank-account
├── src
│   ├── __init__.py
│   ├── amount.py
│   └── personal_account.py
├── uml
│   
└── README.md
```

## Classes

### Amount

- **Attributes:**
  - `amount` (float): The transaction amount.
  - `timestamp` (datetime): The transaction date and time.
  - `transaction_type` (str): The type of transaction ('DEPOSIT' or 'WITHDRAWAL').

- **Methods:**
  - `__init__(self, amount, timestamp, transaction_type)`: Initializes the attributes.
  - `__str__(self)`: Returns a string representation of the Amount object.

### PersonalAccount

- **Attributes:**
  - `account_number` (int): A unique identifier for the account.
  - `account_holder` (str): The name of the account holder.
  - `balance` (float): The current balance in the account.
  - `transactions` (list): A list to store Amount objects.

- **Methods:**
  - `__init__(self, account_number, account_holder)`: Initializes the attributes and sets the balance to 0.0.
  - `deposit(self, amount)`: Deposits money into the account and updates the balance.
  - `withdraw(self, amount)`: Withdraws money from the account if sufficient balance exists.
  - `print_transaction_history(self)`: Prints the transaction history.
  - `get_balance(self)`: Retrieves the current balance.
  - `get_account_number(self)`: Retrieves the account number.
  - `set_account_number(self, account_number)`: Sets the account number.
  - `get_account_holder(self)`: Retrieves the account holder's name.
  - `set_account_holder(self, account_holder)`: Sets the account holder's name.
  - `__str__(self)`: Returns a string representation of the PersonalAccount object.
  - `__add__(self, amount)`: Allows addition of the specified amount to the account.
  - `__sub__(self, amount)`: Allows subtraction of the specified amount from the account.

## UML Class Diagram

The UML class diagram for the project can be found in the `uml/class_diagram.uml` file. It provides a visual representation of the classes, their attributes, methods, and relationships.

## Requirements

To run this project, ensure you have the following dependencies listed in `requirements.txt`.

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run the Python scripts in the `src` folder to manage your personal bank account.

## Test Cases

Test cases can be implemented to verify the functionality of the Amount and PersonalAccount classes. Ensure to cover various scenarios such as deposits, withdrawals, and transaction history retrieval.
