print("Welcome to Kiran Bank")

balance = 10000

print("opening balance: ₹", balance)

while True:
    print("\n----- Kiran bank menu-----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid amount! Enter an amount greater than 0.")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount! Enter an amount greater than 0.")

        elif amount > balance:
            print("Transaction failed: Insufficient balance.")
            print("Current Balance: ₹", balance)

        else:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Updated Balance: ₹", balance)

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice! Please select an option from 1 to 4.")
