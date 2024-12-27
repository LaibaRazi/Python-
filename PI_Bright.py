print("Practise")
print("List in the list we use [] square brackets")

StdListStack = ['Jaweria','Aliya','sanasha','Jaderial',"E2","E3","E4"]
print(",".join(StdListStack))

print("---------------------------------------------------------------")
for i in StdListStack:
    print(i)
print("---------------------------------------------------------------")
print(f"Names Of My Student's are : {', '.join(StdListStack)} .")


groceries = ["Sugar","Masala","Vege","CleaningGoods","CleaningGoods1","CleaningGoods2"]
print(",".join(groceries))
# negative Indexing startes from the end
print(groceries[-1])    #it printed vege because that was the last one

print(groceries[2:])

print(groceries[:3])

rev = ["el1","el2","el3","el4","el5","el6"]
print(",".join(rev))
for send in rev:
    print(send)

print("Printing Should Start from 2nd element from start of the list (Skips first two) syntax is nameoflist[how_many_wanted_to_skip:] ",rev[2:])
print("(Keep first two) Syntax is 'nameoflist[:how_many_wanted_tokeep]':", rev[:2])

print("Wanted to have only last one so do one thing \" NameOfList[-1]\" ",rev[-1])

print("laiba razi KHAN".upper())
print("laiba razi KHAN".lower())
print("laiba razi KHAN".capitalize())

longlist_demo = [[1,2,8],[9,3,4]]
for long in longlist_demo:
    print(long) #
 
print(longlist_demo[0][0],"GIVE ONE FROM LIST".capitalize())
print(longlist_demo[0][2])
print(2**2,"Exponetial works")

poping = rev.pop(2)
print(rev)

this_dic={
    "brand":"lancome",
    "Product":"Mascara"
}
this_tuple = (1,2,3,4,5,6)

print(type(this_dic))
print(type(this_tuple))
print(type(rev))

#making a nested dictionary 
family={
    "child1":{
        "name":"Fatima",
        "age":34,
        
    },
    "child2":{
        "name":"Laiba",
        "age":20,
        
    }
    
}
print(family)

#Revising the concepts.

newL1 = [[1,2,3,4,5],[7,7,6,7,7],[1,6,3,4,2]]
print(type(newL1))

newline = {
    "Child":"FirstValue",
    "2ndChild":"SecondValue"
}
print(type(newline))

new_tup = ("text","text")
print(type(new_tup))

