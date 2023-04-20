"""
Bank Account Class

- Encapsulates the data and methods related to a bank acct.
- This class has two private attributes, __account_number and __balance
    these are hidden from the user and can only be accessed through the public
    methods of the class. i.e. deposit(), withdraw(), and get_balance()

"""


class BankAccount:
    def __init__(self, account_number, balance):
        """
        Class constructor
        initializes the private attributes with values passed as arguments
        """
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        """
        Adds the specified amount to the account balance
        """
        self.__balance += amount
    
    def withdraw(self, amount):
        """
        Subtracts the specified amount from the balance, given that there 
        are sufficient funds available
        """
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
    
    def get_balance(self):
        """
        returns the current balance in the account
        """
        return self.__balance

"""
By encapsulating the data and methods within the class, we have achieved several benefits.

# Security
Since we are using private members, this improves security, as it prevents
unauthorized access and modification of account data.

# Modularity
This class provides a modular and reusable interface for working with bank
accounts, which can easily be extended and modified without affecting other parts
of the program

# Maintainability
This class hides the implementation details of the account data and methods, making
it easier to maintain and debug the code. Any changes or updates to the class can 
be made without affecting other parts of the program, which reduces the risk
of unintended errors.

"""