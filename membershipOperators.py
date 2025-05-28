#membership operator = used o check if an element is present in a sequesnce of (str, list, tuple, sets, dict) using 1. in; 2. not in

word = "APPLE"
letter = input("Guess letter in the secret word: ")
if letter in word:
    print(f"Found {letter}!!")
else:
    print("Not found!")

# if letter not in word:
#         print("Not found!")
# else:
#     print(f"Found {letter}!!")

#set
student_names = {"Spongbob","patrick","sandy"}
student = input("Guess name in the student names: ")
if student in student_names:
    print(f"Student {student} exists")
else:
    print(f"{student} does not exist")

# if student not in student_names:
#     print(f"{student} does not exist")
# else:
#     print(f" {student} exists")

#dictionary
student_grades = {"Sandy":"A", "Squidward":"B","SpongeBob":"C","Patrick":"D"}

student = input("Enter the name of a student:")
if student in student_grades:
    print(f"{student} grade: {student_grades.get(student)}")
else:
    print(f"{student}'s grade not found")

email = "annniepauline.23@gmail.com"

if "@" in email and "." in email:
    print("Valid email!")
else:
    print("Invalid email")