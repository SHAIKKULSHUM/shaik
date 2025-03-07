class ParentClass:
    def __init__(self):
        self.__private_field = "private class"

    def __private_method(self):
        return "This is a private method"

    def main_method(self):
        print(self.__private_field)
        print(self.__private_method())

class SubClass(ParentClass):
    def try_access_private(self):
        try:
            print(self.__private_field)
        except AttributeError:
            print("Cannot access private field from subclass")

        try:
            print(self.__private_method())
        except AttributeError:
            print("Cannot access private method from subclass")

if __name__ == "__main__":
    parent = ParentClass()
    parent.main_method()

    sub = SubClass()
    sub.try_access_private()
