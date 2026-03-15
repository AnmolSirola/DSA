# Instance variables belong to each object separately.
# Class variables are shared by all objects of the class.

class Student:

    school = "ABC School"  # class variable shared by all objects

    def __init__(self, name):
        self.name = name   # instance variable unique to each object


s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)
print(s2.name)

print(Student.school)  # accessing class variable