def value_in_group(value, group):
    # defines a function to check whether a value exists in a group
    if value in group:
        # checks whether the value is present in the list
        return True
        # returns True if the value is present
    else:
        return False
        # returns False if the value is not present
print(value_in_group(3, [1, 5, 8, 3]))
# checks whether 3 is present in the list and displays the result
print(value_in_group(-1, [1, 5, 8, 3]))
# checks whether -1 is present in the list and displays the result