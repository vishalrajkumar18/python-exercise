a = int(input("Enter first number: "))
# gets the first number
b = int(input("Enter second number: "))
# gets the second number
c = int(input("Enter third number: "))
# gets the third number
if a == b or b == c or a == c:
# checks whether any two numbers are equal
    print(0)
 # displays zero if any two numbers are equal
else:
    print(a + b + c)
 # adds and displays all three numbers