#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception
# if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, message="age must be at least 18"):
        super().__init__(message)
        
# function check age

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"\nInvalid age: {age}. Age must be atleast 18.")
    print("Age is vaalid.")
    
    # example with error
try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Caught an exception: {e}")