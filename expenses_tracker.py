from datetime import date
present_date = date.today()
print("\nWelcome to the Day to Day Expenses Tracker")
total = 0
expense = {}
incomes = {}

def expenses():
    global total
    text = input("\nEnter Text : ")
    price = int(input("Enter Price : "))
    expense[text] = price
    if total < price:
        print(f"\nyou don't have sufficient money. You have only {total} rs !So Why you are giving much money to shopkeeper")
    elif total > 0:
        total -= price
        print("\nExpenses Add Successfully")
    else:
        print("\nYou Don't have enough money! Please add some income first")
    
def income():
    global total
    text = input("\nEnter Text : ")
    price = int(input("Enter Price : "))
    incomes[text] = price
    if total >= 0:
        total += price
    print("\nIncome Add Successfully")

def view_balance():
    global total
    total_expense = 0
    total_income = 0

    for j in incomes:
        print(f"Income [{j} = {incomes[j]} rs] on Date {present_date.day}/{present_date.month}/{present_date.year}")
        total_income = incomes[j] + total_income 
    print(f"\nTotal Income is = {total_income} rs\n")
    
    for i in expense:
        print(f"Expenses [{i} = {expense[i]} rs] on Date {present_date.day}/{present_date.month}/{present_date.year}")
        total_expense = expense[i] + total_expense 
    print(f"\nTotal Expenses is = {total_expense} rs")
    
    
    # print(f"Your Income Data is : {incomes}")
    print(f"\nYour Total balance is = {total} rs")


for i in range(100):
    print("\n1 = Add Expenses\n2 = Add Income\n3 = View Balance\n4 = Quit")
    value = int(input("==> "))
    if value == 1:
        expenses()
    elif value == 2:
        income()
    elif value == 3:
        view_balance()
    elif value == 4:
        print("\nThanks For choosing Day to Day expenses")
        exit()
    else:
        print("\nPlease Choose the Option Correctly")
        # raise Exception("\nPlease Choose the Option Correctly")
    