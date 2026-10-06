#  List and Tuple generator
# accepts comma-separated numbers from the user and creates both a List and a Tuple.
#  str.split() method, tuple() constructor, list & tuple data types
# /get comma-separated numbers as a single string from user
a = input("Enter numbers: ")
# /split the string by commas into individual items stored in a list
b = a.split(",")
# /display the generated list (mutable sequence)
print("List :", b)
#  /convert the list to a tuple (immutable sequence) and display it
print("Tuple :", tuple(b))