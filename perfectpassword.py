def pass(password):
    lower = False
    upper = False
    digit = False

    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True

    password = input("Enter a password to check: ")
if pass(password):
    print("Password is valid!")
else:
    print("Password must contain at least one lowercase letter, one uppercase letter, and one number.")
