def show_menu():
    print("\n--- 💰 Personal Finance Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Check Balance & History")
    print("4. Exit")

def main():
    balance = 0
    history = []

    while True:
        show_menu()
        choice = input("\nKya karna chahte ho? (1-4): ")

        if choice == '1':
            amount = float(input("Income amount enter karein: "))
            source = input("Paisa kaha se aaya? (e.g., Salary, Gift): ")
            balance += amount
            history.append(f"✅ Added: +₹{amount} ({source})")
            print("Income add ho gayi!")

        elif choice == '2':
            amount = float(input("Kharcha (Expense) amount enter karein: "))
            reason = input("Paisa kaha kharch hua? (e.g., Food, Rent): ")
            if amount > balance:
                print("⚠️ Warning: Aapke paas itne paise nahi hain!")
            else:
                balance -= amount
                history.append(f"❌ Spent: -₹{amount} ({reason})")
                print("Expense record ho gaya!")

        elif choice == '3':
            print(f"\n--- 📊 Current Balance: ₹{balance} ---")
            print("Transaction History:")
            if not history:
                print("Abhi tak koi transaction nahi hua.")
            for item in history:
                print(item)

        elif choice == '4':
            print("Bye! Apne paise dhyan se kharch karna. 👋")
            break
        
        else:
            print("Invalid choice! Dubara try karein.")

if __name__ == "__main__":
    main()