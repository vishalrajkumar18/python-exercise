import os
# imports os module to inspect file system paths
full_path = os.path.realpath(__file__)
# retrieves the absolute path of the currently executing file
file_name = os.path.basename(__file__)
# retrieves the name of the currently executing file
print("File Path:", full_path)
# displays full file path
print("File Name:", file_name)
# displays file name
