import os
# imports os module to interact with the file system
path = "."
# specifies the current directory
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
# filters and lists only files (excluding subdirectories)
print("Files in current directory:")
for f in sorted(files):
    # prints each file name
    print(f)
