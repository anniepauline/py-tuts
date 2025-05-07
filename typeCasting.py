#typecasting - converting var from one data type to another
name  = "Annie Pauline"
age = 24
gpa = 3.2
is_student = True

#get the type of var
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# float to int
gpa = int(gpa)
print (gpa)

#int to float
age = float(age)
print(age)

#float to str
age = str(age)
print(type(age))

#type error
#age+=1
#print(age)

age+="1"
print(age)

#str to bool- False if empty str, True !empty
name = bool(name)
print(name)


