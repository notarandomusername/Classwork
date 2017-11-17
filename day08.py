#Snippet 1:
def say_hello():
    """Print hello."""
    print("Hello!")

say_hello()

#Snippet 2:
def fifty():
    """Returns 50."""
    return 50

print(fifty() * 2)

#Snippet 3:
def add_them_all(n1,n2,n3,n4,n5):
    """Returns the sum of five numbers."""
    return n1 + n2 + n3 + n4 + n5

print(add_them_all(1,3,5,2,100))

#Find hypotenuse problem:
#Imports the math library, and by proxy, the sqrt function.
import math

#Define the side lengths.
a = int(input("Side A:" ))
b = int(input("Side B:" ))

def find_hypotenuse(a,b):
    """Calculate the hypotenuse of two side lengths."""
    c = math.sqrt(a ** 2 + b ** 2)
    print(c)

#Call the function.
find_hypotenuse(a,b)