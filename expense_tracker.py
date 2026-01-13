expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['category']} - ₹{e['amount']}")

def total_expense():
    total = sum(e["amount"] for e in expenses)
    print("Total Expense: ₹", total)

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
