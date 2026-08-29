def get_expense_number(expenses):
    expense_number = int(input("Enter expense number: ")) - 1

    if expense_number < 0 or expense_number >= len(expenses):
        raise IndexError("Invalid Expense Number.")

    return expense_number

def get_valid_amount():
    while True:
        amount = float(input("Enter Expense Amount: "))

        if amount <= 0:
            print("The amount should be greater than 0.")
        else:
            return amount

def get_choice(options, obj):
    while True:
        choice = input("Enter your choice: ")

        if choice in options:
            method = getattr(obj, options[choice])
            method()

            break
        else:
            print("Please enter a valid option.")
