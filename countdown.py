import time

# my_time = int(input("Enter time time in seconds: "))
# for x in range(0,my_time):
#     time.sleep(1)
# print("TIME'S UP!")

# # count backward
# my_time = int(input("Enter time time in seconds: "))
# for x in range(my_time,0,-1): #-1 for decreement
#     print(x)
#     time.sleep(1)
# print("TIME'S UP!")

#count bavkeards
my_time = int(input("Enter time time in seconds: "))
for x in reversed(range(0,my_time)): # range(0, 5) generates [0, 1, 2, 3, 4] rev [4, 3, 2, 1, 0]
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") #- If seconds is less than 10, it will be padded with a leading zero. - If seconds is 10 or more, it remains unchanged.
    time.sleep(1)
print("TIME'S UP!")
