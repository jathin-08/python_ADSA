'''
__init__():  It is a Special kind of method. 
class Empl:
    def __init__(self):
        pass
emp = Empl()
emp1 = __init__()   #Wrong

#self --> Represent the Current Object
class Student:
    def display(self):
        pass

s1 = Student()
s2 = Student()

# self --> s1
# self --> s2
'''

def add(a,b):
    return a + b 
res = add(10,20)
print(res)
 
class Add:
    def add(self,a,b):
        return a + b
res1 = Add()
print(res1.add(10,20))

#Write a Program to find the Area and Perimeter of a Circle
class Circle:
    radius = 5
    def display(self, radius=None):
        if radius is not None:
            self.radius = radius
        else:
            self.radius = Circle.radius
    def Area(self):
        res = (3.14 * self.radius * self.radius)
        print(res)
    def Peri(self):
        res = (2 * 3.14 * self.radius)
        print(res)

c = Circle()
c.display()
c.Area()
c.Peri()

# Leet Code : 1603
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        '''self.big = big
        self.medium = medium
        self.small = small  '''
        self.spaces = [0,big,medium,small]      

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType] >=1:
            self.spaces[carType] -= 1
            return True
        return False
        '''if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
        return False'''