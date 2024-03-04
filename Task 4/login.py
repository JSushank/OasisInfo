import hashlib

# Dictionary to store user credentials (username: password_hash)
user_credentials = {}

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_credentials[username] = hashed_password
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Hash the provided password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in user_credentials and user_credentials[username] == hashed_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def secured_page():
    print("Welcome to the secured page!")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                secured_page()
                break
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
