import sys

def main():
    if len(sys.argv) <= 1:
        print("No arguments provided.")
        return
    
    # Users can add an expense with a description and amount.
    if sys.argv[1] == "add":
        print("Adding an expense...")
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
    else:       print("Unknown command.")


if __name__ == "__main__":
    main()
