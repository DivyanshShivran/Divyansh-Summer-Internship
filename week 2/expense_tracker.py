
def show_menu():
    print("\n=== EXPENSE TRACKER MENU ===")
    print("1. View All Expenses")
    print("2. Add New Expense")
    print("3. View Category Summary")
    print("5. Exit")


def main():
    expenses = [
        {"amount": 250.0, "category": "Food", "description": "Lunch at cafeteria"},
        {"amount": 1200.0, "category": "Transport", "description": "Monthly travel pass"},
        {"amount": 150.0, "category": "Snacks", "description": "Tea and biscuits"}
    ]
    
    valid_categories = ["Food", "Transport", "Snacks", "Entertainment", "Bills", "Other"]

    while True:
        show_menu()
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            print("\n--- ALL EXPENSES ---")
            if not expenses:
                print("No expenses recorded yet.")
                continue
                
            total_spent = 0.0
            for index, exp in enumerate(expenses, start=1):
                print(f"{index}. [{exp['category']}] {exp['description']}: ₹{exp['amount']:.2f}")
                total_spent += exp['amount']
            
            print("-" * 30)
            print(f"Total Combined Expenditure: ₹{total_spent:.2f}")

        elif choice == "2":
            print("\n--- ADD NEW EXPENSE ---")
            print("Available Categories:", ", ".join(valid_categories))
            
            category = input("Enter category: ").strip().capitalize()
            if category not in valid_categories:
                category = "Other"

            try:
                amount = float(input("Enter amount (₹): "))
                if amount <= 0:
                    continue
            except ValueError:
                continue

            description = input("Enter brief description: ").strip()
            if not description:
                description = "Unspecified Expense"

            new_expense = {"amount": amount, "category": category, "description": description}
            expenses.append(new_expense)
            print(f"Added successfully: ₹{amount:.2f} under {category}.")

        elif choice == "3":
            print("\n--- CATEGORY SUMMARY ---")
            if not expenses:
                continue

            summary = {cat: 0.0 for cat in valid_categories}
            grand_total = 0.0

            for exp in expenses:
                cat = exp["category"]
                summary[cat] += exp["amount"]
                grand_total += exp["amount"]

            for cat, total in summary.items():
                if total > 0:
                    percentage = (total / grand_total) * 100
                    print(f" * {cat}: ₹{total:.2f} ({percentage:.1f}%)")

        elif choice == "5":
            break


if __name__ == "__main__":
    main()