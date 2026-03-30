any = "python is a programming language"
vowel_cou = 0
space_cou = 0
con_cou = 0
for i in any :
    if j in "AEIOUaeiou":
     vowel_con += 1
    elif j == "":
        space_cou += 1
print(f"this is count of all vowel in the string {vowel_cou}")
print(f"this is the count of all space in the string {space_cou}")
print(f"this is cons_in the string {len(any)-(vowel_con + space_cou)}")

#RANGE
-------- THIS IS USED TO GENERATE THE NUMBERS\
         SYNTAX----> (START,END,STEP)
         
for i in range(0,14):
    print(i)
   
any = "ram"
print(list(any.replace("rajesh","ram")[0:3]))
print(tuple(any))

a,b = 1,2 
vs = str(vs)
print(type(vs))
print(vs)
print(tuple(an))

rev_str = "rajesh"
re = ""
for i in rev_str:
   re =  i + re
print(re)
if rev_str is re :print("palindrome")
else:print("not")

for num in range(1,50):
    if num * 2 == 0:
        print(f"{num}is a even number")
    else:
        print(f"{num} is a odd number")
