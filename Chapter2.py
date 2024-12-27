from math import *
# number1 = int(input("Enter your first number : "))
# number2 = int(input("Enter your second number : "))
# ans = number1%number2
# if ans == 0 :
#     print("It has Zero remainder")
# else :
#     print("Modulus is ",str(ans))


def magic_function(UserInput):
    
    if isinstance(UserInput,int):
        return f"This is a int {UserInput}"
    elif isinstance(UserInput,float):
        return f"This is a float {UserInput}"
    elif isinstance(UserInput,str):
        return f"This is a string {UserInput}" 
    else:
        return f"Unsupported type"
    
UserInput= input("Enter you Number or String : ")

try:
    if '.' in UserInput:
        UserInput=float(UserInput)
    else:
        UserInput=int(UserInput)
except ValueError:
    pass
        
if isinstance(UserInput,int) :
    UserInput = sqrt(UserInput)
    
print(magic_function(UserInput))
    

# Giveyournumber=float(input("Enter the Number: "))
# writeacolor=input("Enter the color : ")

# print(floor(Giveyournumber))
# print(ceil(Giveyournumber))
# print(fabs(Giveyournumber))
# # print(factorial(Giveyournumber))
# print("Color you entered was",writeacolor)


UserString= '''Writing this whole thing.\n\tAs a whole project use this whole text'''
print(UserString.replace('whole','orange'))

list1=["apple","Soya","Sun",6,9,7,False,"K"]
inputtext=input("Enter You Magic : ")
list1.append(inputtext)
print(list1)


