"""
multi
line
comments

"""
'''
another way
'''
# single line
'''
for i in range(10):
    if i%2 == 0:
        print("even numbers",i)
    else:
        print('odd numbers',i)
'''
# Python OOP's:
# Define  A Class 
''' Sytanx:
class ClassName():
    attributes
    methods

class Students1():
    pass

class Students2:
    pass

class Students3(object):
    pass



print("Students1",issubclass(Students1,object))
print("Students2",issubclass(Students2,object))
print('Students3',issubclass(Students3,object))
'''
# Normal Function
def fun_name():
    pass

# Class Methods

"""Syntax
class myclass:
    def fun_name(self):
        pass
"""

'''
class Car():
    def disp_properties(self):
        print("it is a moving vehical")
class MyClass:
    def my_method(self):
        return "this is my class method"

obj = MyClass()
print(obj)
print(obj.my_method())

# Static methods

class MyClass:
    @staticmethod
    def my_method():
        return "this is my class method"

obj = MyClass()
print(obj)
print(obj.my_method())

# Attributes
class Student:
    roll_num = 0 #class attributes
    name = ""
    def disp_details(self):
        return self.roll_num, self.name


obj = Student()
print(obj.disp_details())
# local variable
class Student:
    roll_num = 0 #class attributes
    name = ""
    def disp_details(self, roll_num,name):
        return roll_num, name
    def checking(self):
        return self.roll_num, self.name

obj = Student()
print(obj.disp_details(12,"person1"))
print(obj.checking())

# Local, Global and class variables
a = 1 # Global variable
b = 2 
class Myclass():
    i = 3 # class variable
    j = 4
    def method(self, m, n):
        print("local m,n", m,n)
        print("Class variable",self.i,self.j)
        print("Global variables", a,b)

variable = Myclass()
variable.method(10,20)

# Local, Global and class variables with same names
a = 1 # Global variable
b = 2 
class Myclass():
    a = 3 # class variable
    b = 4
    def method(self, a, b):
        print("local m,n", a,b)
        print("Class variable",self.a,self.b)
        print("Global variables", globals()['a'],globals()['b'])

variable = Myclass()
variable.method(10,20)
# Constructor
class Student():
    name = ""
    branch = ""
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    def disp(self):
        return self.name, self.branch

obj = Student('ravi', 'cse')
print(obj.disp())
# __str__
class TempClass():
    def __str__(self):
        return "this is a temporary class"


b = TempClass()
print(b)
# inheritance
class  A():
    pass
class parent():
    pass
class child(parent):
    pass
class A():
    def m1(self):
        return "class A Method m1"
class B(A):
    def m2(self):
        return "Class B Method m2"
# accessing parent class methods in child class
class parent():
    def m1(self):
        return "parent class m1"
class child(parent):
    def m2(self):
        super().m1()
        return "child Class m2"
obj1 = child()
print(obj1.m2())

# Accessing Attributes from Parent class
class Class1:
    a = 100
    b = 2000

class Class2(Class1):
    def m1(self):
        result = super().a + super().b
        return result
'''

class Class1:
    a = 100
    b = 2000

class Class2(Class1):
    a = 333
    b  = 444
    def m1(self, a, b):
        print(a,b)
        print(self.a,self.b)
        print(super().a,super().b)

obj = Class2()
obj.m1(77,66)




























































































































































