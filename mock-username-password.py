from hashlib import md5
from getpass import getpass
import sys

print("Hello! Welcome to FaceSnap!") 

attempts = 0
check_username = "5945261a168e06a5b763cc5f4908b6b2"
check_password = "48d6215903dff56238e52e8891380c8f"
# These hashes have been generated earlier on.
# This is not how you would go about storing usernames and passwords,
# but for the sake of simplicity, we'll do it like this.

while True: 
    username = input("Username: ")
    password = getpass("Password: ")
    # Getpass will not echo input to the screen, so your password remains 
    # invisible
    print()

    if attempts == 3:
        sys.exit("Too many failed attempts.")

    if md5(username.encode().hexdigest()) == check_username:
        if md5(password.encode().hexdigest()) == check_password:
            print("Username and password entered correctly.")
            # Username and password match - do something here
        else:
            print("Password entered incorrectly.")
            attempts += 1
    else:
        print("Username entered incorrectly.")
        attempts += 1