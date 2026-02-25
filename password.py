password = input("Enter your password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True   # Anything not letter or digit

if len(password) >= 8 and upper and lower and digit and special:
    print("Strong Password ")
else:
    print("Weak Password ")
