#To use pi in the most correct way, we import math.
from math import pi

#Create a class file for all of the math operations.
class circleMath():
    """Base class for circle math."""

    #Initialize the objects necessary for the math operations.
    #Make sure to include the self parameter, as it is required.
    def __init__(self, r):
        """Initialize the radius attribute."""
        self.radius = r

    #Define functions for the math operations you need.
    def find_circumference(self):
        """Find the circumference of a circular shape."""
        self.find_circumference = 2 * pi * self.radius
        print(self.find_circumference)

    def find_area(self):
        """Find the area of a circular shape."""
        self.find_area = pi * self.radius ** 2
        print(self.find_area)

    def find_surface_area(self):
        """Find the surface area of a spherical shape."""
        self.find_surface_area = 4 / 3 * pi * self.radius ** 2
        print(self.find_surface_area)

#Make a circle object with an user-inputted radius.
circle = circleMath(int(input("Choose a radius: ")))

#Print the math operations defined in the class.
print("The circumference of a circle with a radius of", circle.radius, "is:")
circle.find_circumference()

print("The area of a circle with a radius of", circle.radius, "is:")
circle.find_area()

print("The surface area of a sphere with a radius of", circle.radius, "is:")
circle.find_surface_area()