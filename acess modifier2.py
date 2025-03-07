
class MyClass:
    def __init__(self):
        self._protected_variable = "This is a protected variable"
    
    def _protected_method(self):
        return "This is a protected method"
    
    def public_method(self):
        return "This is a public method"


if __name__ == "__main__":
    obj = MyClass()
    print(obj._protected_variable)  
    print(obj._protected_method())  
    print(obj.public_method())      

class MyClass:
    def __init__(self):
        self._protected_variable = "This is a protected variable"
    
    def _protected_method(self):
        return "This is a protected method"
    
    def public_method(self):
        return "This is a public method"

from package1.my_class import MyClass

class AnotherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_protected(self):
       
        print(self.obj._protected_variable)  
        print(self.obj._protected_method())  

if __name__ == "__main__":
    another_obj = AnotherClass()
    another_obj.access_protected()
