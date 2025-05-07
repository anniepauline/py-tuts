name = input("Enter your full name: ")
result = len(name)
print(result)

print(name.find(" ")) # finds first occurance  counts from index 0
print(name.rfind(" ")) # reverse find - finds last occurance

print(name.capitalize()) # capital first letter of a name
print(name.upper())
print(name.lower())
print(name.isdigit()) # returns true if it has only digits
print(name.isalpha()) # returns trus if it has only alphabetical char's 

phone_number=input("Enter your phone number:")
print(phone_number.isdigit())

count = phone_number.count("0")
print(count)

phone_number = phone_number.replace("0"," ")
print(phone_number)

#print(help(str))


username = input("Enter a username: ")
if not username.isdigit:
    print("Username must contain digits")
elif not username.isalpha:
    print("Username must contain alphabets")
elif not username.upper():
    print("Username must contain upper case letters")
elif not username.lower():
    print("username must contain lower case letters")
elif not username.find(" ") == -1:
    print("Cannot contain white spaces")
elif len(username) < 8 or len(username) > 9:
    print("Length shd be 8 chars")
else:
    print("Valid password")