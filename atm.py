
# Simple ATM Simulator

def menu():
    print("\n**** Welcome to ATM Calculator ****")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def check_balance(balance):
    return balance


def deposit_money(amount, balance):
    balance = balance + amount
    print("Money deposited successfully!")
    return balance


def withdraw_money(amount, balance):
    balance = balance - amount
    print("Money withdrawn successfully!")
    return balance


# PIN Login
correct_pin = 4567
balance = 0
attempts = 3

while attempts > 0:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("\nLogin successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN!")

        if attempts > 0:
            print("Attempts remaining:", attempts)
        else:
            print("Account access denied!")

# ATM Operations
if pin == correct_pin:
    while True:
        menu()

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print("Your balance is:", check_balance(balance))

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                balance = deposit_money(amount, balance)
                print("Your balance is:", balance)
            else:
                print("Invalid amount!")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount!")

            elif amount > balance:
                print("Insufficient balance!")

            else:
                balance = withdraw_money(amount, balance)
                print("Your balance is:", balance)

        elif choice == 4:
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")
