"""{value:flag} format a value based what flags are inserted

.(number)f = round to tat many decilmal places
:(number) = allocate that many spaces
:03 = prefix 0 that many spaces
:< = left justify
:> = right justify
:^ = center justify
:+ = plus sign to indicate +ve value
:= = place sign to leftmost position
: = inserts space before positive nums
:, = comma seperator """

price1 = 3.14158
price2 = -987.65
price3 = 12.34

#floating points
print(f"Price 1 is {price1:.1f}")
print(f"Price 2 is {price2:.1f}")
print(f"Price 3 is {price3:.1f}")

#spaces
print(f"Price 1 is {price1:10}") # each valus has a total of 10 spaces
print(f"Price 2 is {price2:10}")
print(f"Price 3 is {price3:10}")

#0 padded
print(f"Price 1 is {price1:010}") # 0 instead of spaces
print(f"Price 2 is {price2:010}") # sayas I want a 10 digit number. when it's not 10 digint prefex 0
print(f"Price 3 is {price3:010}")

# left justofied
print(f"Price 1 is {price1:<10}") 
print(f"Price 2 is {price2:<10}")
print(f"Price 3 is {price3:<10}")

#right justified
print(f"Price 1 is {price1:>10}") 
print(f"Price 2 is {price2:>10}")
print(f"Price 3 is {price3:>10}")

#center justified
print(f"Price 1 is {price1:^10}") 
print(f"Price 2 is {price2:^10}")
print(f"Price 3 is {price3:^10}")

#sign is [reserved 
print(f"Price 1 is {price1:+}") 
print(f"Price 2 is {price2:+}")
print(f"Price 3 is {price3:+}")

#positive numbers
print(f"Price 1 is {price1: }") 
print(f"Price 2 is {price2: }")
print(f"Price 3 is {price3: }")

price1 = 3000.14158
price2 = -9870.65
price3 = 1200.34

#thousand seperator numbers
print(f"Price 1 is {price1:,}") 
print(f"Price 2 is {price2:,}")
print(f"Price 3 is {price3:,}")

#thousand seperator 
#2 decimal points
# if num is positive preceed with +
print(f"Price 1 is {price1:+,.2f}") 
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.2f}")

