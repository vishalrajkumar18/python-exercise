def check_five(a, b):
    # checks if values are equal, sum is 5, or difference is 5
    if a == b or (a + b) == 5 or abs(a - b) == 5:
        return True
        # returns True if any condition is met
    else:
        return False
        # returns False otherwise
print(check_five(7, 2))
# displays True (difference is 5)
print(check_five(3, 2))
# displays True (sum is 5)
print(check_five(2, 2))
# displays True (numbers are equal)
print(check_five(7, 3))
# displays False
