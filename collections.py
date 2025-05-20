""" colleions = variable used to store multiple values
list - [] has duplicates; ordered; mutable
set - {} no duplicates; unordered; immutable(individual elements cant be changed); add/remove(can change elments)
tuple - () has duplicates; ordered; immutable ;faster; faster than list
"""


"""
#list declaration []
fruits = ["orange","apple","banana","coconut"]
print(fruits[::3]) # every 3 rd element beginning from index 3

#list iteration
for fruit in fruits:
    print(fruit)


#all funs for list fruits
print(dir(fruits))
print(len(fruits))

#check if value in collection
print("apple" in fruits) #returns bool

print(fruits[0])

fruits.append("pineapple") # at the end
print(fruits)

fruits.remove("pineapple")
print(fruits)

fruits.insert(0,"pineapple") # at a given position
print(fruits)

fruits.sort() # changes to asc order 
print(fruits)

fruits.reverse() # rev in order of how we places them
print(fruits)

# rev alphabetically - sort and then reverse
fruits.sort()
fruits.reverse()
print(fruits)

# fruits.clear()
# print(fruits)

print(fruits.index("apple")) # reutrns index (zero-based indexing)
#print(fruits.index("kiwi")) # throws error
print(fruits.count("pineapple"))
"""

"""
#SET = unordered, canot change values, but can add/remove {}

fruits = {'orange', 'apple', 'banana', 'coconut'}
print(fruits)

#print(fruits[0])# cannot aindex set
fruits.add("pineapple")
print(fruits)

fruits.add("coconut") # adding duplicates

fruits.remove("pineapple")
print(fruits)

fruits.pop() # remove topelement
print(fruits)

fruits.clear()
print(fruits)

"""
#TUPLES - ordered, unchangable, duplicates allowed, faster than list ()

fruits = ('orange', 'apple', 'banana', 'coconut', 'pineapple')
print(fruits.index("apple"))
print(fruits.count("coconut"))
for fruit in  fruits:
    print(fruit)
    
print(fruits[::-1])
print(fruits[1])

