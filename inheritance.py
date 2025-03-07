#1.A, B and C are classes
class A:
    def show(self):
        print("This is class A")
class B(A):  
    def display(self):
        print("This is class B")
class C(B): 
    def print_msg(self):
        print("This is class C")
obj = C()
obj.show()      
obj.display()   
obj.print_msg() 

#2.A is a super class. B is a sub class of A. C is a sub class of B.  
class A:  
    def show_a(self):
        print("This is class A")
class B(A):  
    def show_b(self):
        print("This is class B")
class C(B):  
    def show_c(self):
        print("This is class C")
obj = C()
obj.show_a()  
obj.show_b() 
obj.show_c()

#3.Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C 
class A:  
    def method1(self):
        print("Method 1 from Class A")
    def method2(self):
        print("Method 2 from Class A")
    def common_method(self):  
        print("Common method from Class A")
class B(A):  
    def method3(self):
        print("Method 3 from Class B")
    def method4(self):
        print("Method 4 from Class B")
    def common_method(self): 
        print("Common method from Class B")
class C(B):  
    def method5(self):
        print("Method 5 from Class C")
    def method6(self):
        print("Method 6 from Class C")
    def common_method(self):  
        print("Common method from Class C")
obj = C()
obj.method1() 
obj.method2()  
obj.method3()  
obj.method4()   
obj.method5()  
obj.method6()  
obj.common_method()

#4.Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance. 
class A:
    def method1(self):
        print("Class A - Method 1")
    def method2(self):
        print("Class A - Method 2")
    def common_method(self):  
        print("Common method in A")
class B(A):
    def method3(self):
        print("Class B - Method 3")
    def method4(self):
        print("Class B - Method 4")
    def common_method(self):  
        print("Common method in B")
class C(B):
    def method5(self):
        print("Class C - Method 5")
    def method6(self):
        print("Class C - Method 6")
    def common_method(self):  
        print("Common method in C")
def main():
    objA = A()
    objA.method1()
    objA.method2()
    objA.common_method()
    objB = B()
    objB.method1()
    objB.method2()
    objB.method3()
    objB.method4()
    objB.common_method()
    objC = C()
    objC.method1()
    objC.method2()
    objC.method3()
    objC.method4()
    objC.method5()
    objC.method6()
    objC.common_method()
main()

#5.Call an overridden method with super class reference to B and C class’s objects 
class A:
    def common_method(self):
        print("method in A")
class B(A):
    def common_method(self):
        print("method in B")
class C(A):
    def common_method(self):
        print("method in C")
obj1 = A()  
obj2 = B()  
obj3 = C()  
obj1.common_method() 
obj2.common_method()  
obj3.common_method()  

#6.Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members 
class Parent:
    value = "I am from Parent"
    def show_value(self):
        print(self.value)
class Child(Parent):
    value = "I am from Child"  
obj1 = Parent()
obj2 = Child()
obj1.show_value()  
obj2.show_value()

