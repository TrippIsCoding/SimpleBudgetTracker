from datetime import datetime
import sqlite3

# This is a simple budget tracker. You can track income, record expenses, and calculate the budget balance.

def initialize_database():
    # This function initializes the SQLite database, creating necessary tables if they don't exist.
    connection = sqlite3.connect("budget_tracker.db")
    cursor = connection.cursor()

    # Create income table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    ''')

    # Create expenses table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        )
    ''')

    connection.commit()  # Save the changes
    connection.close()  # Close the connection


def get_date():
    # This function prompts the user to enter a valid date in MM-DD-YYYY format.
    while True:
        try:
            date = input("Enter date here (MM-DD-YYYY): ")
            date_format = "%m-%d-%Y"
            datetime.strptime(date, date_format)  # Validate format
            return date
        except ValueError:
            print("Invalid date detected. Please re-enter.")


def enter_amount():
    # This function prompts the user to enter a valid monetary amount (greater than zero).
    while True:
        try:
            amount = float(input("Enter amount here: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_total(query):
    # Helper function to retrieve the sum of income or expenses from the database
    connection = sqlite3.connect("budget_tracker.db")
    cursor = connection.cursor()
    cursor.execute(query)
    total = cursor.fetchone()[0] or 0
    connection.close()
    return total


def income_add():
    # This function adds income records to the database
    try:
        amount = enter_amount()
        date = get_date()
        description = input("Enter description here: ")

        connection = sqlite3.connect("budget_tracker.db")
        cursor = connection.cursor()

        query = "INSERT INTO income (amount, date, description) VALUES (?, ?, ?)"
        cursor.execute(query, (amount, date, description))

        connection.commit()
        connection.close()

        print("Income added successfully.")
    except ValueError:
        print("Please enter a valid value.")


def expense_add():
    # This function adds expense records to the database
    try:
        amount = enter_amount()
        date = get_date()
        description = input("Enter description here: ")

        connection = sqlite3.connect("budget_tracker.db")
        cursor = connection.cursor()

        query = "INSERT INTO expenses (amount, date, description) VALUES (?, ?, ?)"
        cursor.execute(query, (amount, date, description))

        connection.commit()
        connection.close()

        print("Expense added successfully.")
    except ValueError:
        print("Please enter a valid value.")


def display_records():
    # This function displays income and expense records in the database
    connection = sqlite3.connect("budget_tracker.db")
    cursor = connection.cursor()

    print("\nHere are your income records:")
    cursor.execute("SELECT * FROM income")
    for row in cursor.fetchall():
        print(row)

    print("\nHere are your expense records:")
    cursor.execute("SELECT * FROM expenses")
    for row in cursor.fetchall():
        print(row)

    connection.close()


# Initialize the database
initialize_database()

while True:
    transaction_type = input("Would you like to add income or expenses? (type 'income' or 'expense'): ").lower()

    # Check for valid transaction type
    if transaction_type not in ["income", "expense"]:
        print("Invalid option. Please type 'income' or 'expense'.")
        continue

    # Add transaction based on user input
    if transaction_type == "income":
        income_add()
    elif transaction_type == "expense":
        expense_add()

    # Fetch totals from the database
    total_income = get_total("SELECT SUM(amount) FROM income")
    total_expenses = get_total("SELECT SUM(amount) FROM expenses")

    # Calculate and display balance
    balance = total_income - total_expenses
    print(f"\nCurrent Balance: ${balance: .2f}\n")

    # Ask if the user wants to input another entry
    repeat = input("Would you like to input another entry? yes or no: ").lower()

    if repeat != "yes":
        # Display all records when the user decides to stop entering new data
        display_records()
        break
