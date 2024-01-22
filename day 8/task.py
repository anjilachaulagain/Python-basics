# ------------------------------------username-------------------------------
def validate_username(username):
    if not username.replace(" ", "").isalpha():
        raise ValueError("Invalid username: Something is Missing")

try:
    username = input("Enter username: ")
    validate_username(username)
    print("Username is valid")
    
except Exception:
    print("ERROR: check your username again")


# ---------------------------------email-----------------------------


def validate_email(email):
    if not email.lower().endswith("@gmail.com"):
        raise ValueError("Invalid email address: Something is Missing")


try:
    email = input("Email Address: ")
    validate_email(email)
    print("Email Address is valid")
    
except Exception:
    print("ERROR: check your email again")


# -----------------------------password----------------------------------------


def validate_password(password):
    if len(password) < 8:
        raise ValueError("Invalid password. It must be at least 8 characters long.")

try:
    password = input("password: ")
    validate_password(password)
    print("Password is valid")

except Exception:
    print("Error: check your password again")