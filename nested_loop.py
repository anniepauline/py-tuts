# loop within a loop
#outer loop:
    #innner loop:

rows = int(input("Enter rows: "))
cols = int(input("Enter the number of cols: "))
symbol = input("Enter your symbol:")

for x in range(0,rows): # 1 to 9
    print(f"Outer loop {x}", end=" ") # end="" changes the default end character from a newline (\n) to nothing
    for y in range(1,cols):
        print(f"inner loop {y}")

for x in range(0,rows): # 1 to 9
    for y in range(0,cols):
        print(f"{symbol:2}", end="") #same line, each symbol having 2 spaces to the right
    print() # new line