books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_name = input("Enter book name: ")
        books.append({"name": book_name, "status": "Available"})
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available in library.")
        else:
            for book in books:
                print(book["name"], "-", book["status"])

    elif choice == "3":
        search_name = input("Enter book name to search: ")
        found = False

        for book in books:
            if book["name"].lower() == search_name.lower():
                print("Book found:", book["name"], "-", book["status"])
                found = True

        if not found:
            print("Book not found.")

    elif choice == "4":
        issue_name = input("Enter book name to issue: ")
        found = False

        for book in books:
            if book["name"].lower() == issue_name.lower():
                found = True

                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        return_name = input("Enter book name to return: ")
        found = False

        for book in books:
            if book["name"].lower() == return_name.lower():
                found = True

                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")

                break

        if not found:
            print("Book not found.")

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")