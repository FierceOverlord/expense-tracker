from storage.storage_factory import StorageFactory
from manager.expense_manager import Expense_Manager
from utilities.validators import get_choice
from constants.Constants import METHODS
from tkinter import filedialog
from manager.presentation.presentation import display_result

source_path = filedialog.askopenfilename(
    title = "Open Expense File",
    filetypes=[
        ("Expense Files", "*.json *.csv"),
        ("JSON Files", "*.json"),
        ("CSV Files", "*.csv")
    ]
)

storage = StorageFactory.create(source_path)

manager = Expense_Manager(storage)


while True:
        print("""
=== Welcome to Expense Tracker ===
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Calculate Expenses
6. Filter by category
7. Convert / Export File
8. Visualize by Category
9. Visualize by Month
10. Visualize Distribution
""")

        try:
        
            result = get_choice(METHODS, manager)

            display_result(result)
                
        except ValueError as e:
            print(f"Error: {e}")

        cont = input("Do you want to continue (y/n): ").lower()

        if cont != 'y':
            break

