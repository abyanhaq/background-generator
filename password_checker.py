import re
pw_checker = re.compile(r"[a-zA-Z0-9$%#@]{8,}/d")

while True:
    try:
        pw = input("Enter a password: ")
        a = pw_checker.search(pw)
        print(a)
        if not a and pw != "BREAK":
            print("Invalid password, please try again")
        elif pw == "BREAK":
            break
        else:
            print("Password accepted. Halting")
            break
    except:
        print("Invalid password")
        continue
