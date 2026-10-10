def concatenate_list(items):
    # defines a function to join all list elements into a string
    result = ""
    # creates an empty string to store the combined elements
    for item in items:
        # takes each element from the list one by one
        result += str(item)
        # converts the element into a string and adds it to the result
    return result
    # returns the final combined string
print(concatenate_list(['Hello', ' ', 'World']))
# calls the function and displays the combined string