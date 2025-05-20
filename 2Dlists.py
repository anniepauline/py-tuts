"""2D LIST = List made of lists"""

fruits = ['orange', 'apple', 'banana', 'coconut', 'pineapple']
vegetables = ['celery','carrots','potatoes']
meats = ["chichken","fish","turkey"]

#groceries = [fruits, vegetables, meats]

groceries = [
    ['orange', 'apple', 'banana', 'coconut', 'pineapple'],
    ['celery','carrots','potatoes'],
    ["chichken","fish","turkey"] ]

""" 
List of tuples
groceries = [
    ('orange', 'apple', 'banana', 'coconut', 'pineapple'),
    ('celery','carrots','potatoes'),
    ("chichken","fish","turkey") 
    ]

    Tupe of tuples
    (
    ('orange', 'apple', 'banana', 'coconut', 'pineapple'),
    ('celery','carrots','potatoes'),
    ("chichken","fish","turkey") 
    )

    Tuple of sets
    (
    {'orange', 'apple', 'banana', 'coconut', 'pineapple'},
    {'celery','carrots','potatoes'},
    {"chichken","fish","turkey"} 
    )
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