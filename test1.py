# / Circle Area Calculator
# / Calculates the area of a circle from user-entered radius.
# / import math, math.pi constant, float() type conversion, arithmetic operators (*)
import math
# / ask the user to enter the radius and convert input string to a float (decimal number)
r = float(input("Enter radius: "))
# / calculate the area using formula: area = pi * r^2
area = math.pi * r * r
#  display the calculated area to the user
print("Area =", area)