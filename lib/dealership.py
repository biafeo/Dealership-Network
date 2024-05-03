class Dealer:
    def __init__(self, name, location, contact, employees):
        self.name = name
        self.location = location
        self.contact = contact
        self.employees = employees

    def __str__(self):
        return f"Dealer Name: {self.name}\nLocation: {self.location}\nContact: {self.contact}\nEmployees: {self.employees}"


class CarType:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Car Type: {self.name}\nDescription: {self.description}"


class Car:
    def __init__(self, make, model, year, price, mileage, color, available, car_type):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.color = color
        self.available = available
        self.car_type = car_type

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nPrice: {self.price}\nMileage: {self.mileage}\nColor: {self.color}\nAvailability: {availability}\nCar Type: {self.car_type}"
    

# Mock Data for testing the classes
dealer = Dealer("ABC Motors", "123 Main St", "123-456-7890", 10)
car_type = CarType("Electric", "Electric cars use electricity for propulsion")
car = Car("Tesla", "Model S", 2022, 80000, 5000, "Red", True, car_type)

print(dealer)
print(car_type)
print(car)