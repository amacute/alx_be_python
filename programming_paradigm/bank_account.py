# bank_account.py

class BankAccount:
    """
    A class to represent a simple bank account.
    Encapsulates account balance and provides methods for deposit, withdrawal,
    and displaying the balance.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account. Defaults to 0.0.
        """
        # Initialize the account_balance attribute
        # Using a private-like convention with __ to suggest encapsulation
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.__account_balance += amount
            # print(f"Deposited: ${amount}. New balance: ${self.__account_balance}") # For internal testing
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif self.__account_balance >= amount:
            self.__account_balance -= amount
            # print(f"Withdrew: ${amount}. New balance: ${self.__account_balance}") # For internal testing
            return True
        else:
            # print("Insufficient funds.") # For internal testing
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}") # Format to 2 decimal places

