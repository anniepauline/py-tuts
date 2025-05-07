#
import math
friends = 3
friends **= friends # to the power
print(friends)

#round
x=3.14
y=4
z=5

# gives abs value
result = round(x*y)
print(result)

#gives +ve value
y=-4
result=abs(y)
print(result)

y=4
#power
result=pow(4,3)
print(result)

#max
result= max(5,64)
print(result)

#min
result= min(5,64)
print(result)

#math editor
print(math.pi)
print(math.e)
result = math.sqrt(x)
print(result)
result=math.ceil(9.1) #rounds up
print(result)
result=math.floor(9.1) #rounds down
print(result)

# 2*pi*r = circum of circle
r = int(input("Enter radius of circle: "))
result = 2*math.pi*r
print(f"the circumference is {round(result,2)}")