"""
this is like switch statement of C & C++
"""
import time
#timestamp in match statment
timestamp = int(time.strftime('%H'))
match timestamp :
    case 00 :
        print("Good Night")
    case _ if timestamp > 00 and timestamp <= 6 :
        print("Hey It's Daw Now")
    case _ if timestamp > 6 and timestamp <= 9 :
        print("Good Morning")
    case _ if timestamp > 9  and timestamp <=15 :
        print("Good AfterNoon")
    case _ if timestamp > 15 and timestamp <= 21 :
        print("Good Evening")
    case _ if timestamp > 21:
        print("Sleep please")
    case _ :
        print("some error is there")

#_____________
x = 0
match x:
    case 0:
        print("x is 0")
    case _:
        print("x is something else")

