# A class method works with class variables rather than instance variables.
# It is defined using the @classmethod decorator.

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name


Student.change_school("XYZ School")

print(Student.school)