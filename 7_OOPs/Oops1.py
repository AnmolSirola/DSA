# We are designing a simple Library System.
# This example demonstrates Encapsulation, Inheritance, Polymorphism and Abstraction.

from abc import ABC, abstractmethod


# Abstraction
# LibraryItem is an abstract class representing any item in the library.

class LibraryItem(ABC):

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True   # Encapsulation: private variable

    def borrow(self):
        if self.__available:
            self.__available = False
            print(f"{self.title} borrowed successfully")
        else:
            print(f"{self.title} is currently unavailable")

    def return_item(self):
        self.__available = True
        print(f"{self.title} returned")

    def is_available(self):
        return self.__available

    @abstractmethod
    def get_details(self):
        pass



# Inheritance
# Book class inherits from LibraryItem.

class Book(LibraryItem):

    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def get_details(self):
        print(f"Book: {self.title} by {self.author}, {self.pages} pages")



# Inheritance
# Magazine class also inherits from LibraryItem.

class Magazine(LibraryItem):

    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue

    def get_details(self):
        print(f"Magazine: {self.title}, Issue {self.issue}")



# Library class manages items

class Library:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            item.get_details()



# Creating objects

book1 = Book("Python Programming", "John Smith", 400)
mag1 = Magazine("Tech Monthly", "Editor Team", 42)


# Polymorphism
# Both objects respond to get_details()

library = Library()

library.add_item(book1)
library.add_item(mag1)

library.show_items()


# Borrow and return

book1.borrow()
book1.borrow()
book1.return_item()