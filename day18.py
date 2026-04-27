'''
#FUNCTIONS
-----------
1.FIND ALL
-----------
--->By using this function, it will find all sequences in the string

SYNTAX
-------     re.findall("metachar",variable_name)
---> By using this function, it will only find sequence in the string


2.SEARCH
----------
----> By using this function, if will only find sequence in the string
syntax
-------  re.search("metachar",var_name)

METACHARACTERS
----------------
----> Metacharacters are used to form searching pattern

import re
so = "By using this function it will find all sequences in the 1,2,3,4,5,"
any = re.findall("[1-5,a-f]", so)
an = re.search("[a]" , so)
print(any)
print(an)

import re
any = "etacharacters are used to form searching patte"
an = re.search("a" , any)
print(an)

# dot(.)
----> this meta character will form a searching pattern as it will take
any single character for(.)

import re
any = "hello guys"
so = re.findall("[h....s]", any)
thing = re.search("he..o" , any)
print(so)
print(thing)

3.^
--> This is used to find the string is starting with the sequence or not

syntax
-------> re.findall("metachar", variable_name)

import re
we = "This is used to find the string is starting with the sequence or not"
want = re.findall("^This " , we)
print(want)

4.$
--> This is used to find the string is ending with the swquence or not
syntyax
-------  re.findall("$",variable_name)

import re
our = "This is my name rajesh"
out = re.findall("rahul $",our)
op = re.search("This is $",our)
print(out)
print(op)


5.*
--> This meta character will form a searching pattern as it will take
any zero or more character for(*)

syntax
-------> re.findall(".*",variable_name)
         re.search(".+",variable_name)


import re
raj = "Metacharacters are used to form searching pattern"
rahul = re.findall("M.*i",raj)
ram = re.search("M.+i", raj)
print(rahul)
print(ram)

6.+
---> This metacharacter will form a searching pattern as it will take
any one or more character for (+)

syntax
------->  re.search(".+",variable_name)
'''
import re
any = "This metacharacter will form a searching pattern as it will take"
so = re.findall("T.+r",any)
print(so)

                    











  





































                 


