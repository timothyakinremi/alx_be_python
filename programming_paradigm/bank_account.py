class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a bank account with an optional initial balance (default is 0)."""
        self.__account_balance = initial_balance  # encapsulated attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.1f}")
            return True
        return False

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        return False

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")  # 👈 EXACT match

    def get_balance(self):
        """Getter for accessing balance securely."""
        return self.__account_balance
