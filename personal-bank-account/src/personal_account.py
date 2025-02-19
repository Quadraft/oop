class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type}: {self.amount}"


class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Amount(amount, 'DEPOSIT'))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Amount(amount, 'WITHDRAWAL'))
        else:
            raise ValueError("Insufficient funds")

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self