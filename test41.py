import os
# imports the os module to interact with the operating system
file_name = "test1.py"
# specifies the file name to check
if os.path.isfile(file_name):
    # checks if the file exists
    print(f"File '{file_name}' exists.")
else:
    print(f"File '{file_name}' does not exist.")
    # displays message if file is not found
