def add_integers(a, b):
    # checks if both objects are integers (and not booleans)
    if isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool) and not isinstance(b, bool):
        return a + b
        # returns the sum if both are integers
    else:
        return "Inputs must be integers!"
        # returns error message if either is not an integer
print(add_integers(10, 20))
# displays 30
print(add_integers(10, 20.5))
# displays Inputs must be integers!
print(add_integers("10", 20))
# displays Inputs must be integers!
