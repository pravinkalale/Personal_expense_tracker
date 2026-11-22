class Expense:
    def __init__(self,expense_id, title, amount, category, date):
        self.expense_id = expense_id
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        
    def display_expense(self):
        print("Expense ID:",self.expense_id)
        print("Title:",self.title)
        print("Amount:",self.amount)
        print("Category:",self.category)
        print("Date:",self.date)