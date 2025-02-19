class Car:
    def __init__(self, company=None, model=None, year=None, price=None):
        self.company = company
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Company: {self.company}, Model: {self.model}, Year: {self.year}, Price: {self.price}")

    def calculate_depreciation(self, current_year):
        if self.year is not None and self.price is not None:
            age = current_year - self.year
            depreciation = self.price * (0.05 * age)
            return max(0, self.price - depreciation)
        return None

class Petrol(Car):
    def __init__(self, company=None, model=None, year=None, price=None, expenses=None):
        super().__init__(company, model, year, price)
        self.expenses = expenses

    def display_info(self):
        super().display_info()
        print(f"Expenses: {self.expenses}")

class Coupe(Car):
    def __init__(self, company=None, model=None, year=None, price=None, seats=None):
        super().__init__(company, model, year, price)
        self.seats = seats

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seats}")

if __name__ == "__main__":
    n = int(input("Enter the number of cars: "))
    cars = []

    for _ in range(n):
        car_type = input("Enter car type (Car, Petrol, Coupe): ")
        company = input("Enter company: ")
        model = input("Enter model: ")
        year = int(input("Enter year: "))
        price = int(input("Enter price: "))

        if car_type.lower() == "petrol":
            expenses = float(input("Enter expenses: "))
            car = Petrol(company, model, year, price, expenses)
        elif car_type.lower() == "coupe":
            seats = int(input("Enter number of seats: "))
            car = Coupe(company, model, year, price, seats)
        else:
            car = Car(company, model, year, price)

        cars.append(car)

    for car in cars:
        car.display_info()
        print()