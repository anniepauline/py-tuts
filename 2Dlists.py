"""2D LIST = List made of lists
set of sets and set of lists are not possible
set_of_lists = {[1, 2], [3, 4]}  # ERROR! TypeError: unhashable type: 'list'
Not possible! Lists are mutable, so they can't be placed inside a set.
set_of_sets = {{1, 2}, {3, 4}}  # ERROR! TypeError: unhashable type: 'set'
- Not possible! Sets are mutable, so they can't be inside another set.since all elements within a set is immutable


why is set of list not possible while tuple of list possible?
In a set all the elements must be imutable, so set of lists is not possible
In a tuple, the tuple itself is immutable(order and length), but the obbjs in them are mutable. 

why is set of sets no possible?
A set itself is mutable, meaning we can add or remove elements. But all elements inside a set must be immutable because Python uses hashing to manage set membership efficiently.
If a set contained another set, the inner set could still change, violating the rule that set elements must be immutable.
Immutable set to the rescue
"""


fruits = ['orange', 'apple', 'banana', 'coconut', 'pineapple']
vegetables = ['celery','carrots','potatoes']
meats = ["chichken","fish","turkey"]

#groceries = [fruits, vegetables, meats]

groceries = [
    ['orange', 'apple', 'banana', 'coconut', 'pineapple'],
    ['celery','carrots','potatoes'],
    ["chichken","fish","turkey"] ]

""" 
list_of_lists = [[1, 2], [3, 4], [5, 6]]
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
list_of_sets = [{1, 2}, {3, 4}, {5, 6}]
tuple_of_lists = ([1, 2], [3, 4], [5, 6])
tuple_of_tuples = ((1, 2), (3, 4), (5, 6))
tuple_of_sets = ({1, 2}, {3, 4}, {5, 6})
set_of_tuples = {(1, 2), (3, 4), (5, 6)}
set_of_lists = {[1, 2], [3, 4]}  # ERROR! TypeError: unhashable type: 'list'
set_of_sets = {{1, 2}, {3, 4}}  # ERROR! TypeError: unhashable type: 'set'
"""

print(groceries[0][4]) #pineapple
print(groceries[1][1]) #carrots
print(groceries[2][2]) #fish

print(groceries) #prints nested list


for collection in groceries : 
    print(collection)

for collection in groceries : 
    for item in collection:
        print(item+" ", end="")
    print()



keypad = [(1,2,3),
        (4,5,6), 
        (7,8,9) ,
        ("*",0,"#")]

for row in keypad:
    for num in row:
        print(num, end=" ")
    print()