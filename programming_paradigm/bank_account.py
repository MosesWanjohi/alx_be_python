class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance
   
    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"
    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return f"Withdrew: ${amount}"
        else:
            return f"Insufficient funds. Account balance is: {self.account_balance}"
    def display_balance(self):
        return f"Your current balance is: ${self.account_balance}"
