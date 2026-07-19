passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_chars = "!@#$%^&*"

for password in passwords:
    print(f"\nChecking password: {password}")

    missing = []

    if len(password) < 8:
        missing.append("At least 8 characters long")

    if not any(char.isupper() for char in password):
        missing.append("At least one uppercase letter")

    if not any(char.islower() for char in password):
        missing.append("At least one lowercase letter")

    if not any(char.isdigit() for char in password):
        missing.append("At least one digit")

    if not any(char in special_chars for char in password):
        missing.append("At least one special character (!@#$%^&*)")

    if len(missing) == 0:
        print("Strong Password")
    else:
        print("Weak Password")
        print("Missing:")
        for requirement in missing:
            print("-", requirement)