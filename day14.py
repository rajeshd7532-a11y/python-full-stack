'''
#constructor(__init__)
------------------------
----> A constructor is a special method used to intialize olbject data
__init__
-----

class student:
    def __init__ (self,name,ID):
        self.name = name
        self.ID = ID

    def display(self):
        print(self.name,self.ID)
stu_1 = student('kanna',567)      
stu_1.display()

#Access specifiers
------------------
1.public
syntax--- name
we can use it anywhere in the program
2.protected
syntax --- name
This is only for internal use
3.private
suntax -- __name
This one is restricted

#self
------ This keyword used to unique
'''
class some:
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"
any = some()
print(any.public)
print(any.protected)    
print(any.private)


















