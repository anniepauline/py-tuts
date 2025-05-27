# Iterables = an obj or collection that can be iterated ine at a time  , allowing it to be iterated over a loop
#list
numbers = [1,2,3,4,5,6,7,8]
print(numbers)

#backwards
for number in reversed(numbers): 
    print(number, end = " ")

print()

#tuples
numbers=(1,2,3,4,5,6,7,8)

for item in numbers:
    print(item, end =" ")

print()

#sets
fruits = {"apple","apple","apple","orange","banana","coconut"}
#sets are not reversible
for fruit in fruits :
    print(fruit)

#strings
name = "Bro Code"
for c in name:
    print(c, end=" ")
print()

#dictionary

mydict = {"A":1, "B":2,"C":3}

for key in mydict:
    print(key)

for v in mydict.values():
    print(v)

for k,v in mydict.items():
    print(f"{k}-{v}")

