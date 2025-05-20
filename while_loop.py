#execute when come condition remains ture

name = input("Enter your name:")

#using if else
# if name == "":
#     print("You did not enter name!")
# else:
#     print(f"Your name is {name}")

#using while
print(f"Enter your name ")
while name == "":
    print("You did not enter your name ")
    name=input("Enter your name:")
print(f"Your name is {name}")


age = int(input("Enter your age "))
while age < 0:
    print("Age cant be negative ")
    age = int(input("Enter your age "))
print(f"You are {age} years old!")


food = input("Enter a food u like (type q to exit):")
while not food == 'q':
    print(f"You like {food}")
    food = input("Enter a food u like (type q to exit):")
print("bye!")

num = int(input("Enter a number between 1 and 10: "))
while num >=1 and num <=10:
    num=int(input("Enter a number"))
    print(f"You entered {num}")
print("Exited!")