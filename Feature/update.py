import json

def update(description, new_amount=None, new_category=None):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        print("No expenses found.")
        return
    
    updated = False
    for expense in expenses:
        if expense["description"] == description:
            if new_amount is not None:
                expense["amount"] = new_amount
            if new_category is not None:
                expense["category"] = new_category
            updated = True
            break
    
    if not updated:
        print(f"No expense found with description: {description}")
        return
    
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    
    print(f"Updated expense: {description} - New Amount: ${new_amount}, New Category: {new_category}")