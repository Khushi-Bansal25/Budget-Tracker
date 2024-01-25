class BudgetTracker:
    def __init__(self):
        self.categories = {}
        self.income = 0
        self.expenses = 0

    def add_income(self, amount):
        self.income += amount
        print(f"Income added: ${amount}")

    def add_expense(self, category, amount):
        if category not in self.categories:
            self.categories[category] = 0
        self.categories[category] += amount
        self.expenses += amount
        print(f"Expense added: ${amount} in {category}")

    def display_summary(self):
        print("\n=== Budget Summary ===")
        print(f"Total Income: ${self.income}")
        print(f"Total Expenses: ${self.expenses}")

        if not self.categories:
            print("No expenses recorded.")
        else:
            print("\nExpense Categories:")
            for category, amount in self.categories.items():
                print(f"{category}: ${amount}")

        balance = self.income - self.expenses
        print(f"\nRemaining Balance: ${balance}")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n=== Budget Tracker Menu ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter income amount: $"))
            budget_tracker.add_income(amount)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: $"))
            budget_tracker.add_expense(category, amount)
        elif choice == '3':
            budget_tracker.display_summary()
        elif choice == '4':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
