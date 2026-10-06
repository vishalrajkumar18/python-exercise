# List and Tuple Generator
# splits a comma-delimited input into a list and converts it into a tuple.
#  input(), str.split(), tuple() type casting
# get comma-separated numbers from the user
data = input("Enter numbers: ")
# break the string at each comma to create a list
list1 = data.split(",")
# convert the list into a tuple
tuple1 = tuple(list1)
# print both collections
print("List :", list1)
print("Tuple :", tuple1)