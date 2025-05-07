age = input("Enter your age:")
age = int(age)


if age >100:
    print("You are over aged!")
elif age < 0:
    print("You are not born yet")
elif age >= 18:
    print("You are qualified !")
else:
    print("You are under aged")



response = input("Would you like food? (Y/N)")
if response == "Y":
    print("Have some food")
else:
    print("no food for you")


name = input("Enter your name:")

if name=="":
    print("You did not type your name")
else:
    print(f"Your name is {name}")


for_sale = True

if for_sale:
    print("This item is for sale")
else :
    print("This item is not for sale")



#PYTHON CALCI

operator = input("Enter a operator(+,-,*,/)")
a = int(input("Enter a digit:"))
b = int(input("Enter a digit:"))


if operator == '+':
    print( a+b)
elif operator == '-':
    print( a-b)
elif operator == '/':
    print( a/b)
elif operator == '*': 
    print( a*b)
else:
    print("Invalid operator!")
