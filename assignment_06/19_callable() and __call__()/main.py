#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method 
# that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Example :
double = Multiplier(2)

# Test with callable()
print(callable(double))  # Output: True

# Call the object like a function
result = double(10)
print(result)            # Output: 20
