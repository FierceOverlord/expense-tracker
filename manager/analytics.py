from datetime import datetime

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

    def calculate_by_category(self):
        category_totals = {}

        for expense in self.expenses:
            category_totals[expense.category] = (
                category_totals.get(expense.category, 0) + expense.amount
            )
        return category_totals

    def calculate_by_month_year(self):
        month_total = {}

        for expense in self.expenses:
            date = datetime.strptime(expense.date, '%Y-%m-%d')
            month_year = date.strftime('%Y-%m')

            month_total[month_year] = (
                month_total.get(month_year, 0) + expense.amount
            ) 

        return month_total