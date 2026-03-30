'''
#VOWEL OR NOT 
vowel_con = input("enter a letter:")
if vowel_con in "AEIOU":
    print("vow")
else:
    print("con")
    
 # TIME LIST
 
Time_aday = input("Enter 24 hours time:")
parts_ =  Time_aday.split(":")
hours_ = int(parts_[0])
min_ = int(parts_[1])
if hours_ >=13 and min_ <60:
    print(f"{Time_aday} convert into {hours_ - 12}:{min_}pm")
else:
    print(f"you have entered nrml or min are incorrect")
  
#LIST--->
EX:-

list_1 = [1,2,3,"python",[1,2,["python","java"],"language"]]
print(list_1[4][2][0][3])

# METHODS OF LIST
---------------------
*APPEND()
*EXTEND()
*REMOVE()
*POP()

list_2 = [1,2,3,4,5,6,7]
print(list_2)
list_2.append(67)
print(list_2)
list_2.append([33,3])
print(list_2)

#EXTEND :-- 

list_3 = [1,2,3,4,5]
list_3.extend([1,22,44,55,"rajesh"])
print(list_3)

#REMOVE----> THIS method will delete the item or value directlty

list_4 = [1,2,3,4,"rajesh"]
list_4.remove(4) 
print(list_4)

# POP----> THIS method will delete the item or value 
'''
list_5 = [1,2,3,4,"raj"]
list_5.pop(4)
print(list_5)

 
