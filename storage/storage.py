import os, json
from models.expense import Expense

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def save_expenses(self, expenses):
        data = []

        for expense in expenses:
            data.append(expense.to_dict())

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_expenses(self):
        data = []

        if not os.path.exists(self.filename):
            return []

        if os.path.getsize(self.filename) == 0:
            return []

        with open(self.filename, "r") as file:
            data = json.load(file)

        expenses = []

        for expense in data:
            expenses.append(
                Expense(
                    expense["title"], 
                    expense["amount"], 
                    expense["category"], 
                    expense["date"]
                )
            )

        return expenses