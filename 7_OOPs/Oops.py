# We are designing a simple Bank System.
# This example demonstrates all OOP concepts:
# Encapsulation, Inheritance, Polymorphism, and Abstraction.

from abc import ABC, abstractmethod


# Abstraction:
# BankAccount is an abstract class.
# It defines the blueprint for all types of bank accounts.

class BankAccount(ABC):

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # Encapsulation: private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def withdraw(self, amount):
        pass


# Inheritance:
# SavingsAccount inherits from BankAccount.

class SavingsAccount(BankAccount):

    def withdraw(self, amount):

        if amount > self.get_balance():
            print("Insufficient balance")

        else:
            # accessing encapsulated balance through method
            new_balance = self.get_balance() - amount
            print(f"{amount} withdrawn from Savings Account")
            print(f"Remaining Balance: {new_balance}")


# Inheritance:
# CurrentAccount inherits from BankAccount.

class CurrentAccount(BankAccount):

    def withdraw(self, amount):

        # Polymorphism:
        # withdraw behaves differently for different account types

        overdraft_limit = 500

        if amount > self.get_balance() + overdraft_limit:
            print("Overdraft limit exceeded")

        else:
            new_balance = self.get_balance() - amount
            print(f"{amount} withdrawn from Current Account")
            print(f"Remaining Balance: {new_balance}")


# Creating objects

savings = SavingsAccount("Anmol", 2000)
current = CurrentAccount("Rahul", 1000)


# Using methods

savings.deposit(500)

print("Savings Balance:", savings.get_balance())

savings.withdraw(1000)

current.withdraw(1200)