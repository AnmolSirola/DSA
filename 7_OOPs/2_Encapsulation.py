# Encapsulation means bundling data and methods together
# and restricting direct access to some variables.

class BankAccount:

    def __init__(self, balance):   # initialize account balance
        self.__balance = balance   # __balance is a private variable

    def deposit(self, amount):     # method to add money
        self.__balance += amount

    def get_balance(self):         # getter method to access private variable
        return self.__balance


account = BankAccount(1000)   # creating object
account.deposit(500)

print(account.get_balance())  # accessing private data via method