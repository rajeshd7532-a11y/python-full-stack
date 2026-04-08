'''breaking it into smaller, simpler, subproblems.
Recursion is especially useful for problems that can be
divided into identical smaller tasks, such as mathemetical


def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("enter 4 digit pin:")
        if len(user_pin) == 4 and user_pin == self.user_info:
            print("welcome")
            return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"invailed pin. attempts left: {self.remaining_attempts}")
            else:
                print(f" card blocked. please contact customer")
                return False
 
any = "python is a language"
vowel_list = []
con_list = []
def vowel_con(any,vowel_list,con_list):
    for i in any:
        if i in "AEIOUauiou":
            vowel_list.append(i)
        else:
            con_list.append(i)

    print(f"{vowel_list} these are all vowel in the string")
vowel_con(any,vowel_list,con_list)

num = 8
count = 0
def prime_check(num,count):
    for i in range(1,num+1):
        if num % i == 0:
            count +=1
        if count == 2:
            print("prime")
        else:
            print("not")

'''

















                  
