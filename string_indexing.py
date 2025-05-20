#Basic Indexing:
#Accessing Elements:
#Use square brackets [] with the index number to retrieve a specific element. For example, my_list[0] accesses the first element of the list my_list.
#Negative Indexing:
#Negative indices count from the end of the sequence. my_list[-1] accesses the last element, my_list[-2] accesses the second-to-last, and so on.


#Slicing [start : end : step]
credit_num = "1234567890123456"
print(credit_num[-1]) # prints last character
print(credit_num[0 : 4]) # ending index is excluded
print(credit_num[5:]) # print everything from index 5
print(credit_num[:4]) # evrything except index 4
print(credit_num[:-1])   # last index of string
print(credit_num[-1:])
print(credit_num[:]) #everything
print(credit_num[::2]) # print every other element/every second starting form the 0th index
print(credit_num[::3])# step over 3 char's staring from the 0th index
print(credit_num[::]) # everything in order
print(credit_num[::-1]) # prints elements n reverse

print(credit_num[1::2]) # print every other element starting from 1st index

#print 1st four digits
print(credit_num[:4])
#last four
print(credit_num[-4:])

