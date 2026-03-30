'''string ----> string is a collaction of char,which represent 
"""or'' and we can access the using indexing[string can also allow   negative index] and  also
slicing.this also immutable,where i could not able to modify

any = 'python programing'
print(any[5])
#so = any.replace("python","java")
#print(any)
#print(so)
len()---> len() method is used to get char present in the string or find the length of the string

a_day = "I'm Rajesh from anakapalli, have 3+ years of exp data science"
print(f"my name is {a_day[4:22:-2]}")

a_day = "rajesh i am from anakapalli"
print(len(a_day))
#length
note :- we can convert a string into integer, if the contain
only integer values....
any = 12234

# split():- remove space , and the is in the list[] it will give the separate 
thing in each index
syntax ---->  variable__name.split("sub string")

#lower()----> this is used to convert all letter into lower case

#SPLIT---->
some = "python is a programming language"
print(some.split(""))

#LOWER---> 

some = "PYTHON programming LANGUAGE"
print(some.lower())

#upper---->

some = "PYTHON PROGRAMMING LANGUAGE"
print(some.upper())

#replace()---> this is used to replace old string and new string
syntax --->variable_name.replace("old string","new string")

'''
some = "python programming language"
print(some.replace("python","java"))
