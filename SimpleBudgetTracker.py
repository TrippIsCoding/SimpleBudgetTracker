#This is a simple budget tracker. You can track income, record expenses, and calculate the budget balance.

def validate_date(date):
    #check's if the date format is correct
        if date[4] == '-' and date[7] == '-' and len(date) == 10 and date[:2].isdigit() and date[3:5].isdigit() and date[6:].isdigit():
            month = int(date[:2])
            day = int(date[3:5])
            year = int(date[6:])
        
          #check's if the month is a valid number
            if 1 <= month <= 12:
            #check's if the day is valid (will be updated to check amount of day's in the month eventually)
              if 1 <= day <= 31:
                return True
              else:
                print("Invalid day. Please enter a valid day (01-31).")
                return False
            else:
                print("Invalid month. Please enter a valid month (01-12).")
                return False
        else:
            print("Invalid date format. Please enter the date in the format MM-DD-YYYY.")
            return False

#get's user's income data
def income_add():
    try:
        amount = int(input("Enter amount here: "))
        description = input("Enter description here: ")
        date = input("Enter a date (MM-DD-YYYY): ")

        if not validate_date(date):
            return None
    
        income_entry = {"amount": amount, "description": description, "date": date}
        print("Income added: ", income_entry)
        return income_entry
    except ValueError:
        print("Please enter a valid value.")
        return
    
#add's every amount input from income_records and returns the total amount
def income_calculator(income_records):
    total_income = sum(entry["amount"] for entry in income_records)
    return total_income
 

#get's user expense data
def expense_add():
   try:
        amount = int(input("Enter amount here: "))
        description = input("Enter description here: ")
        date = input("Enter a date (MM-DD-YYYY): ")

        if not validate_date(date):
            return None

        expense_entry = {"amount": amount, "description": description, "date": date}
        print("Expense added: ", expense_entry)
        return expense_entry
   except ValueError:
        print("Please enter a valid value.")
        return
   
#add's every amount input from expense_records and returns the total amount
def expense_calculator(expense_records):
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
      income_records.append(income_add())
  
  elif transaction_type == "expense":
      expense_records.append(expense_add())

  #get's the total balance
  total_income = income_calculator(income_records)
  total_expenses = expense_calculator(expense_records)

  #subtraces expenses from income
  balance = total_income - total_expenses

  #print's leftover balance
  print(f"Current Balacne: {balance}")

  print("")

  #get's input from user to check if they want to make another entry
  repeat = input("Would you like to input another entry? yes or no: ")

  #check's if the user want's to input another entry
  if repeat.lower() == "yes":
    continue
  elif repeat.lower() == "no":
     print("here are you're income records: ")
     print(income_records)
     print("Here are you're expense records")
     print(expense_records)
     break