from datetime import datetime

#This is a simple budget tracker. You can track income, record expenses, and calculate the budget balance.

def get_date():
  #Validaes the data format and checks for valid month and day
  while True:
    try:
      date = input("Enter date here (MM-DD-YYYY): ")
      date_format = "%m-%d-%Y"
      date_object = datetime.strptime(date, date_format)

      return date
    except ValueError:
       print("Invalid date detected please re-enter.")
       
        
           

#Get's the user to enter a valid monetary amount.
def enter_amount():
  while True:
    try:
      amount = float(input("Enter amount here: "))
      if amount <= 0:
          print("Amount must be greater than zero.")
      else:
          return amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def income_add():
  #Promt's the user to add an income entry.
    try:
        amount = enter_amount()
        description = input("Enter description here: ")
        date = get_date()

        income_entry = {"amount": amount, "description": description, "date": date}
        print("Income added: ", income_entry)
        return income_entry
    except ValueError:
        print("Please enter a valid value.")
        return
    

def income_calculator(income_records):
  #Calculate the total income.
    total_income = sum(entry["amount"] for entry in income_records)
    return total_income
 

def expense_add():
  #Prompt's the user to add an expesne entry
   try:
        amount = enter_amount()
        description = input("Enter description here: ")
        date = get_date()

        expense_entry = {"amount": amount, "description": description, "date": date}
        print("Expense added: ", expense_entry)
        return expense_entry
   except ValueError:
        print("Please enter a valid value.")
        return
   

def expense_calculator(expense_records):
  #calculate the total expense value.
    total_expenses = sum(entry["amount"] for entry in expense_records)
    return total_expenses


#keeps a record of income and expenses
income_records = []
expense_records = []

#loops incase the user wants to input multiple transaction's
while True:
  transaction_type = input("Would you like to add income or expenses? (type 'income' or 'expense'): ").lower()
  
  #add's transaction to the records
  if transaction_type == "income":
      income = income_add()
      if income:
        income_records.append(income)
  
  elif transaction_type == "expense":
      expense = expense_add()
      if expense:
        expense_records.append(expense)

  #get's the total balance
  total_income = income_calculator(income_records)
  total_expenses = expense_calculator(expense_records)

  #subtraces expenses from income
  balance = total_income - total_expenses

  print()

  #print's leftover balance
  print(f"Current Balance: ${balance: .2f}")
  
  print()

  #get's input from user to check if they want to make another entry
  repeat = input("Would you like to input another entry? yes or no: ")

  print()

  #check's if the user want's to input another entry
  if repeat.lower() == "yes":
    continue
  elif repeat.lower() == "no":
     print("Here are you're income records: ")
     print(income_records)
     print()
     print("Here are you're expense records")
     print(expense_records)
     break