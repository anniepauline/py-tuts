""" logical operators: evulate multiple conditions (or, and,  not)"""
""" or = atleast one condition"""
""" and = both conditions """
""" not = inverts the condition """

temp = 25
is_raining =False

if temp < 25 and not is_raining:
    print("Cancelling the outdoor event")
else :
    print("Outdoor event is scheduled")


# conditional expression
num = 5
print("Positive" if num > 0 else "Negative")

result = 9
print("Even" if result % 2 ==0 else "Odd")
print(result)

a = 6
b = 7

max_num =  a if a>b else  b
print(f"Max num is: {max_num}")

min_num = a if a<b else b
print(f"Min num is: {min_num}")