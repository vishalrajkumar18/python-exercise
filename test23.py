s = input("Enter a string: ")
# /gets a string from the user
n = int(input("Enter number of copies: "))
#/gets the number of copies from the user.
if len(s) < 2:
#/Checks whether the string contains fewer than two characters
    result = s * n
#/if the string has fewer than two characters, repeats the entire string n times
else:
    result = s[:2] * n
    #/extracts the first two characters of the string
print(result)