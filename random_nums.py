import random

low = 1
high = 100
options = ["rock","paper","scissors"]
cards = ["2","3","4","5","6","7","8","9","K","J","Q","A"]


num = random.randint(low,high)
print(num)

f_num=random.random()
print(f"Float point nume : {f_num}")

option = random.choice(options)
print(option)

random.shuffle(cards)
print(cards)

