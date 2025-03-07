#2. Call the constructors(both default and argument constructors) of super class from a child class
class Parent:
    def _init_(self, parent_name=None):
        if parent_name is None:
            self.parent_name = "Parent Default"
            print("Parent Default Constructor")
        else:
            self.parent_name = parent_name
            print("Parent Parameterized Constructor:", self.parent_name)

class Child:
    def _init_(self, name=None):
        if name is None:
            self.parent = Parent()
            print("Child Default Constructor")
        else:
            self.parent = Parent(name)
            print("Child Parameterized Constructor:", name)
'''
# Creating instances
child1 = Child()
child2 = Child("ParentName")
#3. Apply private, public, protected and default access modifiers to the constructor
class AccessModifiers:
    def _init_(self):
        print("Public Constructor")

    def protected_constructor(self, name):
        print("Protected Constructor:", name)

    def private_constructor(self, name, id):
        print("Private Constructor:", name, "ID:", id)

# Creating instance and simulating different access levels
obj = AccessModifiers()
obj.protected_constructor("Protected Name")
obj.private_constructor("Private Name", 101)
#4. Write a program which illustrates the concept of attributes of a constructor.
class Student:
    def _init_(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_student(self):
        print("Student Name:", self.name, ", Roll Number:", self.roll_number)

# Creating instance and displaying attributes
student = Student("John Doe", 10)
student.display_student()
'''
