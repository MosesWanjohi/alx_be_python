class BankAccount:
    def __init__(self, account_balance,  initial_balance = 0):
        self.account_balance = account_balance
   
    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"
    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        #f"Withdrew: ${amount}"
        else:
            return False
        #f"Insufficient funds. Account balance is: {self.account_balance}"
    def display_balance(self):
        return (f'Current Balance: ${self.account_balance:.2f}')

