
class MyClass:
    def __init__(self):
        self.public_variable = "This is a public variable"
    
    def public_method(self):
        return "This is a public method"


if __name__ == "__main__":
    obj = MyClass()
    print(obj.public_variable)  
    print(obj.public_method())  



class AnotherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_public(self):
        print(self.obj.public_variable) 
        print(self.obj.public_method())  


if __name__ == "__main__":
    another_obj = AnotherClass()
    another_obj.access_public()



class OtherClass:
    def __init__(self):
        self.obj = MyClass()

    def access_public(self):
        print(self.obj.public_variable) 
        print(self.obj.public_method())  


if __name__ == "__main__":
    other_obj = OtherClass()
    other_obj.access_public()
