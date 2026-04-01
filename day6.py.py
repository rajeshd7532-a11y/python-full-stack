'''table_num = int(input("enter a number:"))
for j in range(1,20):
    print(f"{table_num} x {j} = {table_num*j}")
----->
an = "Python Is a Programming Language"
count_u = 0
count_l = 0
for ch in an:
    if ch.isupper():
        count_u += 1
    elif ch.lower():
        count_l += 1
print(f"there are total {count_u} cap l")
print(f"there are total {count_l} small l")
------>
an = "Python Is a Programming Language"
cap_l = []
small_l = []
for ch in an:
    if ch.isupper():
       cap_l.append(ch)
    elif ch.islower():
        small_l.append(ch)
print(f"{cap_l}cantain all cap l")
print(f"{cap_l}cantain all small s")
 ------>
 ATM
 ------>
sbi_user_details = {"NAME": "rajesh",
                    "ATM PIN": "5522"}
print("welcome to the sbi")
print("plz insert your atm card")
print("check your details")
sbi_user_pin = input("pls enter your 4 digit ATM pin")
if len(sbi_user_pin) == 4:
    if sbi_user_pin in sbi_user_details["ATM PIN "]:
        print("the pin is correct")
    else:
        print("you have entered invailid pin")
else:
    print("plz enter 4 digit pin")
'''
per_num = int(input("enter a number:"))
fact_all = 0
for i in range(1,per_num):
    if per_num % i == 0:
        fact_all +=j
if fact_all == per_num:
    print(f"{per_num} perfect number")
else:
    print(f"{per_num}not a perfect number")


















    
