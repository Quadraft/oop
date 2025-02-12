class Car():
    def __init__(self, company:str, model:str, year:int, price:int ):
        self.company = company
        self.model = model
        self.year = year
        self.price = price
class petrol(Car):
    def __init__(self, expenses:float):
        self.expenses = expenses
class coupe(Car):
    def __init__(self, seats = (2 or 4) ):
        self.seats = seats

        