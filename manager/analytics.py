
class Analytics:
    def __init__(self, expenses):
        self.expenses = expenses

    def total_spending(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount    
        return total    

    def average(self):
        if not self.expenses:
            return 0
        
        return sum(expense.amount for expense in self.expenses) / len(self.expenses)

    def calculate_by_category():
        return

    def calculate_by_month_year():
        return