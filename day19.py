'''
 special sequence
-----------------
A special sequence is a \ followed by one of the character in the
list below, and has a

special meaning
---------------

\A
-----
Return a match if the specified characters are at the brginning
of the string
Eg: "\AThe"


import re
txt = "The rain in spain"
x = re.findall("\AThe",txt)
print(x)
if x:
    print("yes,there is a match")
else:
    print("no match")

\b
----
Returns a match where the specified characters are at the beginning or at the end of a word
Eg: r"\bain"

import re
txt = "the rain in spain"
#check if "is present at the beginning of a word:
x = re.findall(r"\bThe",txt)
print(x)
if x:
    print("yes,there is a match")
else:
    print("no match")
    
\d
----
Returns a match where the string contains digits (numbers from 0-9)

eg:"\d"

import re
txt = "the rain is 676565 spain"
#check if the string contains any digits
x = re.findall("\D",txt)
print(x)
if x:
    print("yes this is match")

else:
    print("no match")
    
\s
----
-->Returns a match where the string  contains a white space'
character

Eg: "\S"

import re
txt = "the rain is 676565 spain"
#check if the string contains any white spaces
x = re.findall("\s",txt)
print(x)
if x:
    print("yes this is match")

else:
    print("no match")


\S
----
-->Returns a match where the string Dose NOt contains a white space'
character

Eg: "\S"


import re
txt = "the rain is 676565 spain"
#check if the string contains any white spaces
x = re.findall("\S",txt)
print(x)
if x:
    print("yes this is match")

else:
    print("no match")


#Time and Date
----------------

%d = Date
%m = Month
%y = Year
%H = Hour
%M = minutes
%S = sec
%P = AM/PM
%A = Day name
%B = Month name
'''
import datetime
now = datetime.datetime.now()
print(now)






























