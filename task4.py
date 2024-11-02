from colorama import Fore


def log_info(msg: str):
    return f"{Fore.BLUE}{msg}{Fore.RESET}"


def log_error(msg: str):
    return f"{Fore.RED}{msg}{Fore.RESET}"


def validate_name(name: str, contacts: dict):
    if name not in contacts.keys():
        return False, log_error("Contact not found")
    return True, "Valid"


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return log_info("Contact added")


def change_contact(args: list, contacts: dict):
    name, phone = args
    valid, e = validate_name(name, contacts)
    if not valid:
        return e

    contacts[name] = phone
    return "Contact changed"


def show_phone(args: list, contacts: dict):
    name, *rest = args
    valid, e = validate_name(name, contacts)
    if not valid:
        return e

    return contacts[name]


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = (
            input(f"{Fore.YELLOW}Enter a command: {Fore.GREEN}").strip().lower()
        )
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            for user in contacts.keys():
                print(f"{user}: {contacts[user]}")
        else:
            print(f"{Fore.RED}Invalid command")


if __name__ == "__main__":
    main()
