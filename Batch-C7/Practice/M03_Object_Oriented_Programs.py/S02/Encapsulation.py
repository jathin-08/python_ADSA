'''
OOP --> 4 Types
1. Encapsulation
2. Inheritance
3. Abstraction
4. Polymorphism

1. Encapsulation : Bundling of data and methods 
Implementation:

Access Modifiers:Access Variables
3 Types
1. Public -->Any one can access these var in entire code
2. Protected --> (_)It can access in a class from another class
3. Private --> (__)
'''
class A:
    name = "Kalyani"    #Public
    _name = "Ram"       #Protected
    __name = "Sai"      #Private
    def display(self, name):
        self.__name = name
a = A()
print(a.name)
print(a._name)
print(a._A__name)

#Write a Program for BankAccount to check balance amount after adding 500 to my acc(1000) 
# ATM -->Machine -->(Accountnumb, balance)
# Hide --> Bank Data DB --> Methods{deposit(),withdraw(),Check_balance()}

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    def display(self):
        return self.__balance
b = BankAccount(1000)
b.deposit(500)

print(b.display())
