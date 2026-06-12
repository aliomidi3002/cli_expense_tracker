import json
from datetime import datetime

# Users can add an expense with a description and amount.
def add(description, amount , category="General"):
    expense = {
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": category  # Default category, can be extended to allow user input
    }
    
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    
    expenses.append(expense)
    
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    
    print(f"Added expense: {description} - ${amount}")
