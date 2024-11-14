#This is a simple budget tracker. You can track income, record expenses, and calculate the budget balance.

#get's the amount, description, and date of the transaction from user
def income_add():
    try:
        amount = int(input("Enter amount here: "))
        description = input("Enter description here: ")
        date = input("Enter date here: ")
    
        income_entry = {"amount": amount, "description": description, "date": date}
        print("Income added: ", income_entry)
        return income_entry
    except ValueError:
        print("Please enter a valid value.")
        return
#keeps a record of ever trasaction
income_records = []

#loops incase the user wants to input multiple transactions
while True:
  income_records.append(income_add())

  print("")

#checks if user wants to keep inputing entries 
  repeat = input("Would you like to input another entry? yes or no: ")

  if repeat.lower() == "yes":
    continue
  elif repeat.lower() == "no":
     print("")
     print(income_records)
     break