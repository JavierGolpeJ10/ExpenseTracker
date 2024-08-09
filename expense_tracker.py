from expense import Expense


def main():
    print(f"Running Expense Tracker!")

    expense_file_path = "expenses.csv"
    # Get user input to get the expense
    expense = get_user_expense()
    # then write it into a cvs file
    save_expense_to_file(expense, expense_file_path)
    #  read file and summarize expenses
    summarize_expense(expense_file_path)


def get_user_expense():
    print("Getting User Expense!")
    expense_name = input("Enter expense name: ")
    expense_ammount = float(input("Enter expense amount: "))
    print(f"You've entered {expense_name}, {expense_ammount}")

    expense_categories = [
        "🍔Food",
        "🏠Home",
        "🏎️Car",
        "💵Savings",
        "🍿Entertainment"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}: {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category name {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_ammount)
            return new_expense
        else:
            print("Invalid selection! Pick again!")


def save_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")


def summarize_expense(expense_file_path):
    print("Summarizing User Expense")


if __name__ == "__main__":
    main()


