import sys
from Feature.add import add

def main():
    if len(sys.argv) <= 1:
        print("No arguments provided.")
        return
    
    # Users can add an expense with a description and amount.
    if sys.argv[1] == "add":
        if len(sys.argv) < 4:
            print("Usage: python main.py add <description> <amount> <category>")
        else:
            description = sys.argv[2]
            amount = float(sys.argv[3])
            category = sys.argv[4] if len(sys.argv) > 4 else "General"
            add(description, amount, category)
    # Users can view all expenses.
    elif sys.argv[1] == "view":
        print("Viewing expenses...")
    # Users can delete an expense.
    elif sys.argv[1] == "delete":
        print("Deleting an expense...")
    # Users can update an expense.
    elif sys.argv[1] == "update":
        print("Updating an expense...")
    # Users can view a summary of all expenses.
    elif sys.argv[1] == "report":
        print("Generating a report...")
    # Users can view a summary of expenses for a specific month (of current year).
    elif sys.argv[1] == "monthly":
        print("Generating a monthly report...")
    # Add expense categories and allow users to filter expenses by category.
    elif sys.argv[1] == "category":
        print("Filtering expenses by category...")
    # Allow users to set a budget for each month and show a warning when the user exceeds the budget.
    elif sys.argv[1] == "budget":
        print("Setting a budget...")
    # Allow users to export expenses to a CSV file.
    elif sys.argv[1] == "export":
        print("Exporting expenses to CSV...")
    else:       
        print("Unknown command.")
        print("usage: python main.py <command> [arguments] <category>")



if __name__ == "__main__":
    main()
