'''
#POLYMORPHISM
--------------
----> This allows a object of different  classes to be treated as an instance of the same base class,
with methods behaving differently based on the actual object type..
eg....
--------
print(Len("python"))
print(Len([1,2,3]))

#METHOD OVERLOADING
--------------------
--->This defines multiple methods with the same name but  different parameter
(number,type, or order) in the same class


class calculator:
    def multiple(self,a,b,c,h):
        return a+b*c-h
cal = calculator()
print(cal.multiple(1,6,2,66))
print(cal.multiple(3,4,5,44))

#METHOD OVERRIDING
-------------------
----> This occurs in the child class, redefining a parent class method with the same signature for runtime

import pyttsx3
engine = pyttsx3.init()

class animal:
    def speak(self):
        return "sound"

class dog(animal):
    def speak(self):
        return engine.say("bow bow")

do = dog()
print(do.speak())
engine.runAndWait()



class someone:
    def __init__(self):
        self.a = a
        self.b = b
    def __add__(self,other):
        return someone(self.a +other.a self.b +other.b)
    def __str__(self):
        return f"((self.a), (self.b))"
any = someone(22,3)
so = someone(5,6)
print(any+so)
    

#DATA ABSTRACTION
------------------
---> This hides complex implementation details, exposing only essential
feactures via abstract class or interface
'''

from abc import ABC, abstractmethod
class shape (ABC):
    @abstractmethod
    def area (self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 *self.radius **2
circle = circle(5)
print(circle.area())
















                
























