
""" types: 1. positional 2.default 3.keyword 4.arbitary"""

import time


def hbd(name, age):
    print(f"Happy birthday {name}. You are {age} years old!" )

hbd("annie", 20)
hbd("steve", 30)
hbd("joe", 40)


def display_invoice(username, amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of amount ${amount:.2f} is due : {due_date}")

display_invoice("annie",30.50,"01/05/2025")


# DEFAULT args = sed when an arg is omitted,shd be at the end
#built in function ex : print("Hello world") end is "/n" by default
""" is used when that arg is omitted, makes fun more flex
types : 1. positional 2. DEFAULT, 3. keyword, 4.arbitrary"""


def net_price(list_price, discount=0, sales_tax=0):
    return list_price *(1-discount) * (1+sales_tax)

print(net_price(500))
print(net_price(500,0.1))
print(net_price(500,0.1,0))

#  default args shd be at the end
def count(end, start=1):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
        
count(5)


# KEYWORD args = the arg has the name of the para when passing data
#buils in example - print("hello", end=" ") 
def hello(greeting, title, firstName, lastName):
    print(f"{greeting} {title} {firstName}  {lastName}")

#hello(greeting="hello",lastName="Annie",firstName ="Pauline",title ="Miss")
#while mixing posiional and keyword ags, make sure positional args are first
hello("hello",firstName="Pauline",lastName="Annie",title="Miss")

print("1","2","3","4","5","6","7","7", sep="-")

for x in range(1,10):
    print(x, end= " ") #example of keyword arg

for x in range(1,10):
    print(x, sep=" ,") # example of keyword args

def get_phone(country, area, first, last):
    print(f"{country}-{area}-{first}-{last}")

get_phone(first=83100, last=21,area=292,country=91)


#arbitary functions = (varying no. of args)

def add(a,b):
    print(a+b)

add(90,8)

# when we have no count for arg
#* args = unpacking operator, for multiple non key args
def addArgs(*args): # args stored in a tuple 
    total = 0 
    for arg in args:
        total+=arg
    print(total)

addArgs(1,2,3,4,5,6,7,8,9)


def dispayName(*args): 
    for arg in args:
        print(arg , end=" ")

dispayName("Annie", "Pauline", "spongebob")

# **kwargs  = keywors args, for multiple keyword args
def printAddress(**kwargs): # the kwargs are stored in a dictoonary
    for value in kwargs.values():
        print(value, end=" ")
    print()
    for key in kwargs.keys():
        print(key, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}-{value}")

printAddress(city="Bangalore",state="Kar",country ="India",continent ="Asia",zipcode="560037")


print()
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    # for key,value in kwargs.items():
    #     print(f"{key}:{value}")
    # if "apt" exists
    if "apt" in kwargs:
        print(kwargs.get("apt"),kwargs.get("state"), kwargs.get("city"), kwargs.get("zipcode"))
    else:
        print(kwargs.get("state"), kwargs.get("city"), kwargs.get("zipcode"))

shipping_label("Annie", "Pauline", "spongebob",city="Bangalore",state="Kar",country ="India",continent ="Asia",zipcode="560037")

