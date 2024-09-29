import time
# timestamphour = int (time.strftime('%H'))
# print(timestamphour)
timestamphour = 13
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
timestamp= time.strftime('%H:%M:%S')
print(timestamp)

if timestamphour >= 12 and timestamphour<=17:
    print("Good AfterNoon")
elif timestamphour<=12 :
    print("Good Morning")
elif timestamphour >= 18 :
    print("Good Evening")
else :
    print("wrong time!")
    

