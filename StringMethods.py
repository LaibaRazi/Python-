#string is immutable however we are getting new string while making it uppercase
#string methods makes another new strings

name="Laiba Razi Khan"
print(name.upper())

name="Laiba Razi Khan!!!!!!!!"
print(name.rstrip("!"))
#rstrip will strip trailing characters

name1 =" Laiba LaibaLLLLLLLLLLL"#characters at the end it gonna strip
print(name1.rstrip("L"))
namestrip= name1.rstrip("L")
print(namestrip)

#Replace is another function
Sent="my name is Laiba and I'm 20 years old and my profession is Making kids learn how to code"
print(Sent.replace("Laiba","Taha")) # it can change all occurance

#practise strings 
stringone= "Getting this string having all \'G\' GGGGGGG"
print(stringone.rstrip("G"))

#string 

nameinput = str(input("Enter Your Name : "))

namestrips=nameinput.rstrip()
print(str(namestrips.capitalize())+" Hey")

#capiltalized

namecap="taha naseem khan"
print(namecap.capitalize()) #only gonna make first alphabet capital 

#split gonna split from there 

print(namecap.replace("naseem","Naseem"))
print(namecap.split(" "))

print(namecap.count("taha"))

#find the number of findings
print(str(namecap.find("a"))+"This is find") #gives the index of first occurance 

#index is similar to find but if we aren't sure about 
print(str(namecap.index("f")+"its index method")) # it will give you an error instead if you have used find it will give you -1
