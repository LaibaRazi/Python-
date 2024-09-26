# # age= int(input("Enter your Age "))

# # if age >= 18 : 
# #     print("You can drive")
# # else :
# #     print("You Can't drive")

# #making a calculator

# print("""Operations Available are listed below :
#       \n 1. to + write \"Add\"
#       \n 2. to - write \"Minus\"
#       \n 3. to x write \"Times\"
#       \n 4. to / write \"Divide\"
#       """)
# op = input("Enter the operation : ")

# if op == "Add" or op == "add" :
#     numberone= int(input("Enter Your First Number : "))
#     numbertwo= int(input("Enter Your Second Number : "))
#     print(str(numberone)+"+"+str(numbertwo)+"="+str(numberone+numbertwo))
# elif op == "Minus" or op == "minus" :
#     numberone= int(input("Enter Your First Number : "))
#     numbertwo= int(input("Enter Your Second Number : "))
#     print(str(numberone)+"-"+str(numbertwo)+"="+str(numberone-numbertwo))
# elif op =="Times" or op =="times" :
#     numberone= int(input("Enter Your First Number : "))
#     numbertwo= int(input("Enter Your Second Number : "))
#     print(str(numberone)+"x"+str(numbertwo)+"="+str(numberone*numbertwo))
# elif op =="Divide" or op =="divide" :
#     numberone= int(input("Enter Your First Number : "))
#     numbertwo= int(input("Enter Your Second Number : "))
#     print(str(numberone)+"/"+str(numbertwo)+"="+str(numberone/numbertwo))
# else :
#     print("Enter correct operator")


## Grading System
print("Enter Your Percentage and We'll tell you your grade! \n")
percent = float(input("Enter your percent: "))

if percent == 100 or percent >= 90:
    print("You Got A+ & Your Percentage was " + str(percent) + "%")
elif percent >= 80 and percent < 90:
    print("You Got B+ & Your Percentage was " + str(percent) + "%")
elif percent >= 70 and percent < 80:
    print("You Got B & Your Percentage was " + str(percent) + "%")
elif percent >= 60 and percent < 70:
    print("You Got C+ & Your Percentage was " + str(percent) + "%")
elif percent >= 50 and percent < 60:
    print("You Got C & Your Percentage was " + str(percent) + "%")
elif percent < 50:
    print("Give the exam again")
else:
    print("Invalid input")

