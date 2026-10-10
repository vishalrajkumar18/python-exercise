import site
# imports site module to locate installed package directories
site_packages = site.getsitepackages()
# retrieves the list of paths to site-packages directories
print("Python site packages locations:")
for path in site_packages:
    # prints each directory path
    print(path)
