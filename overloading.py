# Write two methods with the same name but different number of parameters of same type and call the methods
def add(x, y, z=None):
    if z is None:
        return x + y
    else:
        return x + y + z
print(add(1, 2))  
print(add(1, 2, 3))  

#Write two methods with the same name but different number of parameters of different data type and call the methods

def greet(name, age=None):
    if age is None:
        print(f"Hello, {name}!")
    else:
        print(f"Hello, {name}! You are {age} years old.")

greet("John")
greet("Jane",30)

#Write two methods with the same name and same number of parameters of same type
def greet(name):
    print(f"Hello, {name}!")

def greet(name):
    print(f"Hi, {name}!")

greet("John")
