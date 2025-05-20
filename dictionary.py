"""DICTIONARY - contains {key:value} pairs
                ordered and chagable
                no duplicates """

capitals={"USA":"Washington DC", 
          "INDIA":"NEW Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}


# help(capitals)
# help(dir)

print(capitals.get("USA")) # returns value
print(capitals.get("CN")) # returns None

if capitals.get("JAPAN") == None:
    print("Key does not exist")
else : 
    print("That capital exist")

capitals.update({"Germany":"Berlin"}) #insert/update an existing {k:v}
print(capitals)

capitals.update({"INDIA":"Kolkata"}) #updates
print(capitals)

capitals.pop("China") # pass key
print(capitals)

capitals.popitem() # removes the latest {k:v}
print(capitals)

# capitals.clear()
# print(capitals)

# to get all keys
print(capitals.keys())
# to get all values
print(capitals.values())


for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

#items - returns dictionary in the form of (list of tuples)
print(capitals.items())

for key,value in capitals.items():
    print(f"{key} : {value}")



menu = {"pizza":3.00,
        "Nachos":4.50,
        "popcorn":6.00,
        "chips":2.50,
        "lemonade":3.00,
        "soda":4.24}

cart = []
total = 0

print("------MENU-------")
for key,value in menu.items():
    print(f"{key:10} : {value:.2f}")
print("-----------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None :
        cart.append(food)
        total+= menu.get(food)
        

print( f"You added : {cart}")
print("---------Your bill --------")
for item in cart:
    print(f"{item}  - {menu.get(item)}" )

print("---------------------------")
print(f"Total : ${total}")