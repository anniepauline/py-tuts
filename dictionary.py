"""DICTIONARY - contains {key:value} pairs
   Ordered and changeable
   No duplicates
"""

capitals = {
    "USA": "Washington DC",
    "INDIA": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# help(capitals)
# help(dir)

print(capitals.get("USA"))  # Returns value
print(capitals.get("CN"))   # Returns None

if capitals.get("JAPAN") is None:
    print("Key does not exist")
else:
    print("That capital exists")

capitals.update({"Germany": "Berlin"})  # Insert/update an existing {k:v}
print(capitals)

capitals.update({"INDIA": "Kolkata"})  # Updates
print(capitals)

capitals.pop("China")  # Pass key
print(capitals)

capitals.popitem()  # Removes the last inserted {k:v}
print(capitals)

# capitals.clear()
# print(capitals)

# To get all keys
print(capitals.keys())

# To get all values
print(capitals.values())

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)

# Items - returns dictionary in the form of (list of tuples)
print(capitals.items())

for key, value in capitals.items():
    print(f"{key} : {value}")


# Menu system for ordering food
menu = {
    "pizza": 3.00,
    "Nachos": 4.50,
    "popcorn": 6.00,
    "chips": 2.50,
    "lemonade": 3.00,
    "soda": 4.24
}

cart = []
total = 0

print("------MENU-------")
for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")
print("-----------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)

print(f"You added: {cart}")
print("---------Your Bill --------")
for item in cart:
    print(f"{item}  - {menu.get(item)}")

print("---------------------------")
print(f"Total: ${total:.2f}")