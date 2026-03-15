# Static methods belong to the class but do not depend
# on class variables or instance variables.

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


result = MathUtils.add(5, 7)

print(result)