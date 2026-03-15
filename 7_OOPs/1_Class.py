
# A class is a blueprint for creating objects.
# An object is an instance of a class that contains attributes and methods.

class Car: # class Car: defines blueprint
    def __init__(self, brand, speed): #__init__ initializes object attributes
        self.brand = brand   # self refers to the current object
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h")


car1 = Car("Tesla", 120) # car1 is an object instance
car1.drive()




