stringone="Laiba Razi Khan"
print(stringone[0:3]+" \'It's gonna show\' Lai because L=0 a=1 b=2 and it ends on 3 so it doesn't show that") #slicing string[starting position:ending position]

stringtwo="Coding Instructor"
print(stringtwo[0:len(stringtwo)]+": \n This Going to show \"stringtwo[0:len(stringtwo)]\" the whole string because of the len() method")

#negative indexing is pretty tricky

indexing="hello" # h=0 e=1 l=2 l=3 o=4
print(indexing[-2:] +" index 5-2=3 so the 3 is last l ") #Its doing a math total number of alphabets are 5 then - the first index 5-2=3 so the 3 is last l 
print(indexing[1:-1]) #total length - 1 and then answer is 4 as length was 5 in total => it will print hell

#some methods 

#1. The strip() method removes any whitespace from the beginning or the end:


"""
nm="harry"
print(nm[-4:-2])

----------to solve this step 1:

total length of string - negative number
example harry length is 5 -> 5 - 4 = 1 (Starting value is one)
Now length is 5 -> 5-2 = 3 (Ending value for slice is three now)


----------to solve this step 2:

now the indexing like array of string h=0 a=1 r=2 r=3 y=4
then starting value is 1 so "a" starting and ending value is so it gonna end on first "r"

***********Answer is "ar"

"""

tringone="   Laiba Razi Khan"
print(stringone.strip())

nm="harry"
print(nm[-4:-2])