'''
OOPs --> Object-Oriented Programming System

 Class & Object:

 class--> Blueprint or Template
         --> It contains of some Attributes and Methods
 Object--> Instance of a class

Example: 
class C7:     #Class Creation
    pass
a = C7()     #Object Creation
b = C7()
c = C7()


#C7 --> class
a --> object for class C7

Note: We can create multiple Objects using same class

'''
class Student:
    pass
s1 = Student()
s2 = Student()

s1.name = "kalyani"
s1.roll = 15

s2.name = "ram"
s2.roll = 20

print(s1.name)
print(s1.roll)
print(s2.name)
print(s2.roll)

# what is the purpose of OOP:
# 1. Code Reusability
# 2. Security
# 3. Easy to Maintain

#Types of Variables:
# 3 Types
# 1. Instance Variables --> Variables(inside the Objects)
# 2. Class Variables --> Variables(inside the class)
# 3. Local Variables --> Variables(inside the Methods)

class Student:
    x = "Ram"     #Class Variable
    def display(self):
        name = "C7"     #Local Variable
        print(name)
s1 = Student()
s1.name="sai"      #Instance Variable
print(s1.name)
print(s1.x)
s1.display()
