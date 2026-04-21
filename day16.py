'''
multi level inheritance
------------------------
---> This occurs when a class inherits from a class,createing a
grandfather--->parent ---> child in this structure.

class Grandparent:
    def show_Grandparent(self):
        print("I'm Grandparent")

class parent(Grandparent):
    def show_parent(self):
        print("I'm parent")
        
class child(parent):
    def show_child(self):
        print("I'm child")

any = child()
any.show_Grandparent()
any.show_parent()
any.show_child()

#MOBILE
--------
class mobile:
    def system(self):
        print("mobile system update")

class systemupdate(mobile):
    def update(self):
        print("update mobile")

class restart(systemupdate):
    def restart(self):
        print("mobile restart")

any = restart()
any.system()
any.update()
any.restart()

#HIERCHICAL INHERITANCE
-------------------------
----> This occurs when multiple child classes inherit from a single parent class, this process is called
"HIERCHICAL INHERITANCE"

class parent:
    def parent(self):
        print("I am parent")
class child_1(parent):
    def child_1(self):
        print("I am child_1")
class child_2(parent):
    def child_2(self):
        print("I am second child")
class child_3(child_1,child_2):
    def child_3(self):
        print("I am third child")
any = child_3()
any.parent()
any.child_1()
any.child_2()
any.child_3()
'''
#HYBRID INHERITANCE
--------------------
-----> This is a combination of 2 or more types of inheritance like single inheritance and multiple
inheritance


              
    
        


























    




    










