
#1. Create a program to create two class. 
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model    
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
person1 = Person("Alice", 25)
person1.display_info()
car1 = Car("Toyota", "Camry")
car1.display_info()

#1.1. Create a constructor and a method for each class 
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is now running.")
person1 = Person("Alice", 25)
person1.display_info()
person1.greet()
car1 = Car("Toyota", "Camry")
car1.display_info()
car1.start_engine()

#1.2. Create a _init_.py for adding all packages 
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age   
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model    
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
if _name_ == "_main_":
    person1 = Person("Alice", 25)
    person1.display_info()
    car1 = Car("Toyota", "Camry")
    car1.display_info()

#1.3. Import the respective packages 
import sys
import datetime
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
person1 = Person("Alice", 25)
person1.display_info()
car1 = Car("Toyota", "Camry")
car1.display_info()

#1.4. Call each class by creating an object to it  
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age   
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
person1 = Person("Alice", 25)
person1.display_info()
car1 = Car("Toyota", "Camry")
car1.display_info()

#1.5. Create a program by all the above
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
person1 = Person("Alice", 25)
person1.display_info()
car1 = Car("Toyota", "Camry")
car1.display_info()
