# Simple Banking System in Python
# Code by Dileep

# Display welcome message
print("===== Welcome To My Bank =====")

# Create username and password
# input() is used to take data from the user
name = input("Create Username: ")
password = input("Create Password: ")

# Initial account balance
balance = 0

# Main loop runs until user exits
while True:

    # Display main menu
    print("\n===== Main Menu =====")
    print("1. Login")
    print("2. Exit")

    # Take user's choice
    choice = input("Choose an option: ")

    # Login option
    if choice == "1":

        # Take login credentials
        user = input("Enter Username: ")
        pwd = input("Enter Password: ")

        # Check username and password
        # 'and' means both conditions must be True
        if user == name and pwd == password:

            # f-string used to display username
            print(f"\nWelcome {user}")

            # Bank menu loop
            while True:

                print("\n===== Bank Menu =====")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Logout")

                # Take bank menu option
                option = input("Enter option: ")

                # Show current balance
                if option == "1":
                    print("Current Balance:", balance)

                # Deposit money
                elif option == "2":

                    # Convert input into integer
                    amount = int(input("Enter amount to deposit: "))

                    # Add amount to balance
                    balance += amount

                    print("Money Deposited Successfully")
                    print("Current Balance:", balance)

                # Withdraw money
                elif option == "3":

                    amount = int(input("Enter amount to withdraw: "))

                    # Check sufficient balance
                    if amount <= balance:

                        # Deduct amount from balance
                        balance -= amount

                        print("Money Withdrawn Successfully")
                        print("Remaining Balance:", balance)

                    else:
                        print("Not Enough Balance")

                # Logout from bank menu
                elif option == "4":
                    print("Logged Out Successfully")

                    # break exits current loop
                    break

                # Invalid bank menu option
                else:
                    print("Invalid Option")

        # Wrong login details
        else:
            print("Incorrect Username or Password")

    # Exit program
    elif choice == "2":
        print("Thank You For Visiting My Bank")

        # Stop program
        break

    # Invalid main menu choice
    else:
        print("Invalid Choice")
        
        
        
        
        # Sample Output
        
        '''
        Create Username: dileep
Create Password: 1234

1. Login
2. Exit

Choose an option: 1

Enter Username: dileep
Enter Password: 1234

Welcome dileep

--- Bank Menu ---
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Logout

Enter option: 2
Enter amount to deposit: 5000

Current Balance: 5000
        '''