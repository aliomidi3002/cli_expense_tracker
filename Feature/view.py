import json

def view(category=None):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            if not expenses:
                print("No expenses found.")
                return
            for expense in expenses:
                if category is None or expense['category'] == category:
                    print(f"{expense['date']}: {expense['description']} - ${expense['amount']} (Category: {expense['category']})")
    except FileNotFoundError:
        print("No expenses found.")