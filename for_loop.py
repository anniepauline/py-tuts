"""can iterate over range, string, sequence...
range(start, end, step)
range stops before the end i.e end - 1"""

for x in range (1,11,2):
    print(x)
print("HAPPY NEW YEAR")

for x in reversed(range(1,11,3)):
    print(x)

credit_card="1234-5678-9012"
for x in credit_card:
    print(x)

for x in range (1,11):
    if x == 3:
        continue
    print(x)

for x in range (1,11): #- range(1, ) generates [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
- 
    if x == 3:
        break
    print(x)

