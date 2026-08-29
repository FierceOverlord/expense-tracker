import os, json, csv
from models.expense import Expense
from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def save_expenses(self, expenses):
        pass

    @abstractmethod
    def load_expenses(self):
        pass

class JSONStorage(Storage):

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

class CSVStorage(Storage):

    def __init__(self, filename):
        self.filename = filename

    def save_expenses(self, expenses):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(
                file, 
                fieldnames=["title", "amount", "category", "date"]
            )
            writer.writeheader()

            for expense in expenses:
                writer.writerow(expense.to_dict())

    def load_expenses(self):
        expenses = []

        if not os.path.exists(self.filename):
            return []
        
        if os.path.getsize(self.filename) == 0:
            return []

        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(
                    Expense(
                        row["title"], 
                        float(row["amount"]), 
                        row["category"], 
                        row["date"]
                    )
                )