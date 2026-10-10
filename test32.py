import getpass
def get_username():
    # gets the current username
    return getpass.getuser()
print(get_username())
# displays the current username