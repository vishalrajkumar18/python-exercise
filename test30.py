a = int(input("Enter first number: "))
# gets the first number
b = int(input("Enter second number: "))
# gets the second number
lcm = max(a, b)
# starts checking from the larger number
while lcm % a != 0 or lcm % b != 0:
    # checks whether both numbers divide the LCM exactly
    lcm += max(a, b)
    # adds the larger number
print("LCM:", lcm)
# displays the LCM