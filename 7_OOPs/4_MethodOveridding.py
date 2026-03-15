# Method overriding happens when a child class provides
# its own implementation of a method already defined in the parent class.

class Animal:

    def speak(self):
        print("Animal makes a sound")


class Cat(Animal):

    def speak(self):   # overriding parent method
        print("Cat meows")


cat1 = Cat()

cat1.speak()  # calls overridden method