'''
class bankac:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = bankac(15000)
acc.deposite(7000)
print(acc.get_balance())


Inheritance
------------
---> This allows a child class (subdclass) to acquire the attributes and method
of a parent class(base class) this is called Inheritance

1.Single Inheritance
---------------------
---> using singlemethod of the class from base class is single Inheritance

2.Multiple

super()
--------
this class is used to call  merthod of the parent class from the child class

class parent:
    def display(self):
        print("this is parent method")

class child(parent):
    def display(self):
        super().display()
        print("this is child method")
name = child()
name.display()
'''
class father:
    def skill_1(self):
        print("father: hard worker")

class mother:
    def skill_2(self):
        print("mother:cooking")

class child(father,mother):
    def all_skills(self):
        print("child: coder")
name = child()
name.skill_1()
name.skill_2()
name.all_skills()









