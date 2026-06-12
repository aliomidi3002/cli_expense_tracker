import json

def delete(description):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print("No expenses found.")
        return
    
    updated_expenses = [expense for expense in expenses if expense["description"] != description]
    
    if len(updated_expenses) == len(expenses):
        print(f"No expense found with description: {description}")
        return
    
    with open("expenses.json", "w") as file:
        json.dump(updated_expenses, file, indent=4)
    
    print(f"Deleted expense with description: {description}")