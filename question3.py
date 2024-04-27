# Task 1
def parse_command(user_input):
    predefined_commands = ["help", "issue", "contact support"]
    for command in predefined_commands:
        if command in user_input.lower():
            return command
    return None

# Task 2
def categorize_issue(user_input):
    categories = {
        "login": ["login", "signin", "authentication"],
        "performance": ["performance", "slow", "lag"],
        "error": ["error", "bug", "crash"],
        "others": ["other", "general"]
    }
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in user_input.lower():
                return category
    return "others" 

def main():
    user_input = input("How can I assist you? ")

    # Task 1
    command = parse_command(user_input)
    if command:
        print(f"Command found: {command}")
        if command == "help":
            print("Here is some helpful information.")
        elif command == "contact support":
            print("You can contact our support team at support@example.com.")

    # Task 2
    if "issue" in user_input.lower():
        category = categorize_issue(user_input)
        print(f"Issue category: {category}")

if __name__ == "__main__":
    main()
