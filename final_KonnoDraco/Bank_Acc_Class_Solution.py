class BankAccount:
    """
    A simple bank account class.
    """
    def __init__(self, owner_name, initial_balance=0):
        """
        Initialize a bank account.
        Parameters:
        owner_name (str): Name of account owner
        initial_balance (float): Starting balance (default 0)
        """
        self.owner_name = owner_name
        self._balance = initial_balance
        # Store owner_name and balance as instance variables
    def deposit(self, amount):
        """
        Add money to the account.
        Parameters:
        amount (float): Amount to deposit
        Returns:
        float: New balance after deposit
        """
        if amount > 0:
            self._balance += amount
        else:
            print("Error: Deposit amount must be positive.")
        return self._balance

    def withdraw(self, amount):
        """
        Remove money from the account if sufficient funds exist.
        Parameters:
        amount (float): Amount to withdraw
        Returns:
        float: New balance after withdrawal
        Returns current balance unchanged if insufficient funds
        """
        if amount <= self._balance:
            self._balance -= amount
        else:
            print(f'Insufficient funds, current balance is {self._balance}')
        return self._balance
        # Check if balance >= amount
        # If yes, subtract amount from balance
        # If no, print "Insufficient funds"
        # Return the balance
    def get_balance(self):
        """
        Get current balance.
        Returns:
        float: Current balance
        """
        self._Current_balance = self._balance
        return self._Current_balance

# Test code (don't modify):
account = BankAccount("John", 100)
print(account.deposit(50)) # Should print: 150
print(account.withdraw(30)) # Should print: 120
print(account.withdraw(200)) # Should print: "Insufficient funds" then 120