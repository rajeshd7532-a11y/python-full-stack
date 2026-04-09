'''
lambda function()
-------------------
---->this is also called anonynous function  

any = lambda so : so + 10
print(any(6))

some = lambda an,so,do : (so-an)*do
print(some(4,9,2))

many = lambda so,an,do,they : (they-so*an)+ an+they *5
print(many(2,3,5,9))

sure = lambda this,these,there,when : (when-these*this+there)% there +5
print(sure(4,5,9,2))

l# list comprehension
-----------------------
--> This is offers the shorter syntax when you want to create a new list
from the existing list..

syntax
--------
 variable_name = [expression loop and andtion]
 
old = [1,2,3,4,5]
new = [j for j in old if j%3!=0]
print(new)
'''
sbi_atchuth_ = {"name" : "Rajesh",
                "atm pin" : "9949",
                "balance" : 10000}
user_pin = input("enter 4 digit pin: ")
if len(user_pin) == 4:
    if user_pin in sbi_atchuth_['atm pin']:
        user_choice = int(input("enter  \n1. withdraw: "))
        if user_choice == 1:
            money_w = int(input("enter money you want to withdraw "))
            if money_w <= sbi_atchuth_["balance"]:
                sbi_atchuth_['balance'] -= money_w
                print(sbi_atchuth_['balance'])
            
               















