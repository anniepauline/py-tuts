
def hbd(name, age):
    print(f"Happy birthday {name}. You are {age} years old!" )

hbd("annie", 20)
hbd("steve", 30)
hbd("joe", 40)


def display_invoice(username, amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of amount ${amount:.2f} is due : {due_date}")

display_invoice("annie",30.50,"01/05/2025")


#default args
""" is used when that arg is omitted, makes fun more flex
types : 1. positional2. DEFAULT, 3. keyword, 4.arbitrary"""


def net_price(list_price, discount=0, sales_tax=0):
    return list_price *(1-discount) * (1+sales_tax)

print(net_price(500, 0, 0.05))