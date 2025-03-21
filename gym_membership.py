import time
from os import system, name


def clear_screen():
    """Clears the terminal screen."""
    system('cls' if name == 'nt' else 'clear')


class Member:
    def __init__(self, first_name, last_name, member_id, status="inactive"):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.member_id = member_id
        self.status = status.lower()

    def display_member(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"ID: {self.member_id}")
        print(f"Status: {self.status.upper()}")
        print("-" * 20)


def create_member(members):
    # Validate First Name
    while True:
        first_name = input("Enter first name: ").strip()
        if first_name:
            break
        print("First name cannot be empty")

    # Validate Last Name
    while True:
        last_name = input("Enter last name: ").strip()
        if last_name:
            break
        print("Last name cannot be empty")

    # Validate Member ID
    while True:
        member_id = input("Enter member ID: ").strip()
        if not member_id:
            print("Member ID cannot be empty")
            continue
        # Check for duplicate ID
        if any(m.member_id == member_id for m in members):
            print("This Member ID already exists. Please choose a different one.")
        else:
            break

    # Validate Membership Status
    while True:
        status = input(
            "Enter membership status (active/inactive): ").strip().lower()
        if status in ["active", "inactive"]:
            break
        else:
            print("Invalid status. Please enter 'active' or 'inactive'.")

    # Create and add member
    new_member = Member(first_name, last_name, member_id, status)
    members.append(new_member)
    print("Member added successfully!")
    time.sleep(1.5)


def search_member(members):
    print("""Search by:
1. Membership ID
2. First Name
3. Membership Status""")

    while True:
        choice = input("Enter your choice: ").strip()
        if choice in ("1", "2", "3"):
            break
        print("Invalid choice. Please select 1-3.")

    if choice == "1":
        search_id = input("Enter Membership ID: ").strip()
        results = [m for m in members if m.member_id == search_id]
    elif choice == "2":
        first_name = input("Enter First Name: ").title().strip()
        results = [m for m in members if m.first_name == first_name]
    else:
        while True:
            status = input("Enter Status (active/inactive): ").strip().lower()
            if status in ["active", "inactive"]:
                break
            print("Invalid status. Please enter 'active' or 'inactive'.")
        results = [m for m in members if m.status == status]

    if results:
        for member in results:
            member.display_member()
    else:
        print("No members found.")
    time.sleep(2)


def display_all(members):
    if not members:
        print("No members registered.")
        time.sleep(2)
        return

    print("Members List:")
    print("-" * 40)
    for member in members:
        member.display_member()
    print("-" * 40)
    time.sleep(3)


def main():
    members = []
    menu_options = {
        "1": ("Add new member", lambda: create_member(members)),
        "2": ("Display all members", lambda: display_all(members)),
        "3": ("Search for a member", lambda: search_member(members)),
        "4": ("Exit", None)
    }

    while True:
        clear_screen()
        print("Welcome to Gym Membership Management")
        print("Please choose an option:")
        for key, (desc, _) in menu_options.items():
            print(f"{key}. {desc}")

        choice = input("Enter your choice: ").strip()

        if choice == "4":
            print("Exiting...")
            time.sleep(1)
            break
        elif choice in menu_options:
            action = menu_options[choice][1]
            if action:
                action()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1.5)


if __name__ == "__main__":
    main()
