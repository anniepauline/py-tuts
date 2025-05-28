# script1.py
import script1

print(f"Current value of __name__: {__name__}")  # This will be "__main__" since test_import.py is run
print(f"Current value of script1.__name__: {script1.__name__}")  # This should be "script1"