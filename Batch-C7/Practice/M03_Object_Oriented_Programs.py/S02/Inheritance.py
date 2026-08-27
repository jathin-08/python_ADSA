'''
Inheritance -->One class can inherit Properties of another class
1. Super class /Base Class / Parent  class : Properties
2. Sub class /Derived class / Child class : 

Types : 5 
1. Single
2. Multi-level
3. Multiple
4. Hierarchical 
5. Hybrid

1. Single Inheritance: One Child with one Parent
Dia:

One Parent 
    |
    |
One Child
Ex:
'''
class Parent:      #One Parent
    def display(self):
        print("This is a Parent class")
class child(Parent):    #One Child
    def display2(self):
        print("This is a Child class")
c = child()
c.display2()
c.display()

# 2. Multi-level Inheritance: 
# Dia:
# 
# One GrandParent 
#     |
#     |
# One Parent
#     |
#     |
# One Child 

class Grand:
    def C7(self):
        print("This is a Grand PArent")
class Parent(Grand):
    def sound(self):
        print("This is a PArent")
class Child(Parent):
    def study(self):
        print("This is a Child Class")
c1 = Child()
c1.C7()
c1.sound()
c1.study()

# 3. Hierarchical Inheritance: 
# Dia:
# 
# One Parent
#     |
#     |
# One or more Child
        
class Parent:
    def Car(self):
        print("This is a parent")
class child1(Parent):
    def Study1(self):
        print("This is 1st child")

class child2(Parent):
    def Study2(self):
        print("This is 2nd child")

a = child1()
b = child2()
a.Car()
a.Study1()

b.Car()
b.Study2()

# 4. Multiple Inheritance: 
# Dia:
# 
# two or more Parent
#     |
#     |
# One Child      

class Father:
    def land(self):
        print("Father's land")
class Mother:
    def land(self):
        print("Mother's Car")
class child(Father,Mother):
    def Property(self):
        print("Child Property")
c = child()
c.land()

# MRO --> Method Resolution Order
