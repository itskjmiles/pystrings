import re

# Task 1
def validate_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Error: Both first name and last name should be at least 2 characters long.")
    else:
        print("Name length validation successful.")

# Task 2
def check_password_complexity(password):
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long.")
    elif not re.search("[a-z]", password):
        print("Error: Password must contain at least one lowercase letter.")
    elif not re.search("[A-Z]", password):
        print("Error: Password must contain at least one uppercase letter.")
    elif not re.search("[0-9]", password):
        print("Error: Password must contain at least one number.")
    else:
        print("Password complexity check successful.")

# Task 3
def format_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, email):
        print("Email format validation successful.")
    else:
        print("Error: Invalid email format.")

def main():
    # Task 1
    print("Task 1: Input Length Validator")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    validate_name_length(first_name, last_name)

    # Task 2
    print("\nTask 2: Password Complexity Checker")
    password = input("Enter your password: ")
    check_password_complexity(password)

    # Task 3
    print("\nTask 3: Email Formatter")
    email = input("Enter your email address: ")
    format_email(email)

if __name__ == "__main__":
    main()
