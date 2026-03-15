# Polymorphism means the same method name can behave differently
# depending on which object is calling it.

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def make_sound(animal):  # function using polymorphism
    animal.sound()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)