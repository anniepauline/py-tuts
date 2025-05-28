# __name __ tells u which file is being executed
#py script run directly =? __name__ = __main__
# py script is imported, __name__ is set to module name(file's name) 
#we use this when we want code/fun from another file but we dont wanna run the main body of another file
# functions and classes  in this module can be reused without the main block of the code executing
# good oractise - modular code, redability, leaves no global vars, avoid unintended execution

#ex = import a library, and use its functions
#when running lib directly display help page

# script1.py

def greetings(name):
    print(f"Current value of __name__: {__name__}")  # This will show "__main__" if run directly
    print(f"Hello {name}!")

def goodbye(name):
    print(f"Bye {name}!")

# This block runs only if script1.py is executed directly, not when imported
if __name__ == "__main__":
    greetings("Annie")