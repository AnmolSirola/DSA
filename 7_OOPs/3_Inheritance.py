# Inheritance allows a class to reuse properties and methods from another class.
# The parent class is called the base class and the child class inherits from it.

class Animal:  # parent class

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):  # Dog inherits from Animal

    def bark(self):
        print("Dog barks")


dog1 = Dog()   # object of child class

dog1.speak()   # inherited method from parent
dog1.bark()    # child class method