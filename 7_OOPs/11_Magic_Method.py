# Magic methods are special methods with double underscores
# that allow operator overloading and object behavior customization.

class Book:

    def __init__(self, title):
        self.title = title

    def __str__(self):   # defines how object prints
        return f"Book title is {self.title}"


b = Book("Deep Learning")

print(b)