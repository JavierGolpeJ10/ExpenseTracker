class Expense:

    def __init__(self, amount, category, name):
        self.amount = amount
        self.category = category
        self.name = name


    def __repr__(self):
        return f'Expense: {self.name}, {self.category}, ${self.amount:.2f}'