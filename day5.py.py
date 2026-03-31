'''prime_num = int(input("enter a prime number"))
count = 0
for j in range(1,prime_num+1):
    if prime_num % j == 0:
        print(j)
        count +=1
        print(count)
if count == 2:
    print(f"{prime_num} is a prime number")
else:
    print(f"{prime_num} is not a prime number")
    
# PRIME NUMBER
---------------
for an in range(1,10):
    for j in range(1,an+1):
        if an % j == 0:
            print(j)

---->
for an in range(2,100):
    count = 0
    for j in range(1,an+1):
        if an % j == 0:
            count += 1
        if count == 2:
            print(f"{an} is a prime")
        else:
            print(f"{an} is not a prime")

----->

list_1  = [1057,197,9,86,1767]

for an in list_1:
          count = 0
          for i in range(1,an+1):
              if an % i == 0:
                  count += 1
          if count == 2:
                print(f"{an} is a prime number")
          else:
                print(f"{an} is not a prime number")

'''
any = [2,3,4,5,3,8,9]
empty = []
for j in any:
    if j not in empty:
        empty.append(j)
        print(empty)
    
    
        
    











