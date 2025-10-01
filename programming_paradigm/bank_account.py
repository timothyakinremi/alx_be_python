class BankAccount():
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        # Depositing money into the bank account
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    def withdraw(self, amount):
        # Withdrawing money from the bank account if funds are sufficient.
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    def dispaly_balance(self):
        # Display the updated account balance
        print(f"Current balance: ${self.account_balance: .2f}")
        
    def get_balance(self):
        # Accessing balance after transactions
        return self.account_balance
        