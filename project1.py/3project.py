# -------- Expense Tracker (Single File Project) --------

FILE = "expenses.txt"

def add_expense():
    name = input("Expense name: ")
    amount = input("Amount: ")
    date = input("Date (DD-MM-YYYY): ")

    with open(FILE, "a") as f:
        f.write(f"{date},{name},{amount}\n")

    print("✅ Expense added!\n")


def view_expenses():
    total = 0
    try:
        with open(FILE, "r") as f:
            print("\n--- All Expenses ---")
            for line in f:
                date, name, amount = line.strip().split(",")
                print(f"{date} | {name} | ₹{amount}")
                total += int(amount)
        print("--------------------")
        print("Total Spent: ₹", total, "\n")
    except FileNotFoundError:
        print("❌ No expenses found\n")


while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose (1-3): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("👋 Bye Bye")
        break
    else:
        print("❌ Invalid choice\n")
