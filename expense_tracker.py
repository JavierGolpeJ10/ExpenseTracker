from expense import Expense
import datetime
import calendar


def main():
    print(f"Running Expense Tracker!")

    # expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input to get the expense
    expense = get_user_expense()

    # then write it into a cvs file
    save_expense_to_file(expense)

    # determine the file path for the current month to summarize expenses
    expense_file_path = get_monthly_file_path()

    #  read file and summarize expenses
    summarize_expense(expense_file_path, budget)


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


def save_expense_to_file(expense):
    expense_file_path = get_monthly_file_path()

    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")


def get_monthly_file_path():
    current_date = datetime.date.today()
    month = current_date.strftime("%B")
    year = current_date.strftime("%Y")

    month_file = f"expenses_{month}_{year}.csv"

    return month_file


def summarize_expense(expense_file_path, budget):
    print("⏳Summarizing User Expense")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                category=expense_category,
                amount=float(expense_amount),
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by category 📈")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([expense.amount for expense in expenses])
    print(f"📉You've spent ${total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"✅Remaining budget: {remaining_budget}")

    # Step 1: Get the current date
    today = datetime.date.today()
    # Step 2: Determine the last day of the current month
    _, last_day_of_month = calendar.monthrange(today.year, today.month)
    # Step 3: Calculate the remaining days
    remaining_days = last_day_of_month - today.day
    print(f"Remaining days in the current month: {remaining_days}")

    daily_budget = remaining_budget/remaining_days
    print(green(f"Budget Per day: {daily_budget:.2f}"))


def green(text):
    return f"\033[32m{text}\033[0m"


if __name__ == "__main__":
    main()


