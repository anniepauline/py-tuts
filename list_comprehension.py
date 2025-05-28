#list comprehension - [return expression for item in iterable if condition(optional)]


doubles=[]

for x in range(1,11):
    doubles.append(x*2)
    print(x, end=" ")

print()
#using list iterableS:
doubles = [x*2 for x in range(1,11)]
print(doubles)

triples = [y*3 for y in range(1,11)]
print(triples)

squares = [z*z for z in range(1,11)]
print(squares)

# fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in ["apple","orange","banana","coconut"]]
print(fruits)

fruit_chars = [fruit[0] for fruit in ["apple","orange","banana","coconut"]]
print(fruit_chars)

#if condition
numbers = [1,-2,3,-4,5,-6, -7, 8]
positive_nums = [num for num in numbers if num >= 0] # return num if it's +ve
print("Positive numbers: ", positive_nums)

negative_nums = [num for num in numbers if num <0]
print("Negative numbers: ", negative_nums)

even_numbers = [num for num in numbers if num%2==0]
print("Even numbers: ", even_numbers)

odd_numbers = [num for num in numbers if num%2 != 0]
print("Odd numbers: ", odd_numbers)


grades = [85, 79, 42, 56, 61, 30]
passing_grades = [ grade for grade in grades if grade >=60]
print(passing_grades)