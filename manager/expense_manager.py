from models.expense import Expense
from datetime import datetime
from manager.analytics import Analytics
from utilities.errorHandlers import handle_errors
from utilities.validators import *
from utilities.resultFormat import print_format
from constants.Constants import ANALYTICS

class Expense_Manager:
    def __init__(self, storage):
        self.storage = storage
        self.expenses = self.storage.load_expenses()
    
    def add_expense(self):
        title = input("Enter your Expense Title: ")

        amount = get_valid_amount()

        category = input("Enter Category: ")

        now = datetime.now()
        date = now.strftime("%Y-%m-%d")

        self.expenses.append(Expense(title, amount, category, date))
        self.storage.save_expenses(self.expenses)

    @print_format
    def view_expenses(self): 
        return self.expenses
        
    @handle_errors
    def update_expense(self):
        expense_number = get_expense_number(self.expenses)
        
        print("""
What do you want to update?
1. Title 
2. Amount
3. Category
""")

        choice = int(input("Enter your Choice: "))

        if choice == 1:
            new_title = input("Enter new title: ")
            self.expenses[expense_number].title = new_title

        elif choice == 2:
            new_amount = get_valid_amount()
            self.expenses[expense_number].amount = new_amount

        elif choice == 3:
            new_category = input("Enter new category: ")
            self.expenses[expense_number].category = new_category

        else:
            print("Invalid Choice.")
            return
        
        self.storage.save_expenses(self.expenses)

        return "Expense Updated."

    @handle_errors
    def delete_expense(self):
        self.view_expenses()
        expense_number = get_expense_number(self.expenses)
        del self.expenses[expense_number]
        self.storage.save_expenses(self.expenses)

        return "Expense Deleted."

    def calculate_expenses(self):
        analytics = Analytics(self.expenses)

        print("""
Choose an option from below:
1. Total Spending
2. Average
3. Calculate By Category
4. Calculate By Month/Year        
""")

        return get_choice(ANALYTICS, analytics)

    @print_format
    def filter_by_category(self):
        category = input("Enter your category: ").lower()

        return [
            expense
            for expense in self.expenses
            if expense.category.lower() == category.lower()
        ]