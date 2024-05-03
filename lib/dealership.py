import ipdb

class Dealer:
    def __init__(self, name, location, contact, employees):
        self.name = name
        self.location = location
        self.contact = contact
        self.employees = employees
        self.inventory = []  

    def add_car(self, car):
        self.inventory.append(car)

    def __str__(self):
        return f"Dealer Name: {self.name}\nLocation: {self.location}\nContact: {self.contact}\nEmployees: {self.employees}"

class Car:
    def __init__(self, make, model, year, price, mileage, color, available, car_type_name, car_type_description):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.color = color
        self.available = available
        self.car_type_name = car_type_name  # Car type name attribute
        self.car_type_description = car_type_description  # Car type description attribute

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nPrice: {self.price}\nMileage: {self.mileage}\nColor: {self.color}\nAvailability: {availability}\nCar Type: {self.car_type_name}\nDescription: {self.car_type_description}"

# Mock Data for testing the classes
dealer1 = Dealer("ABC Motors", "123 Main St", "123-456-7890", 10)
dealer2 = Dealer("XYZ Autos", "456 Elm St", "987-654-3210", 8)

car1 = Car("Tesla", "Model S", 2022, 80000, 5000, "Red", True, "Electric", "Electric cars use electricity for propulsion")
car2 = Car("Ford", "Mustang", 2020, 60000, 2000, "Blue", True, "Gasoline", "Traditional gasoline-powered car")
car3 = Car("BMW", "i3", 2019, 55000, 3000, "White", False, "Electric", "Electric cars use electricity for propulsion")

dealer1.add_car(car1)
dealer1.add_car(car2)
dealer2.add_car(car3)

print(dealer1)
for car in dealer1.inventory:
    print(car)

print(dealer2)
for car in dealer2.inventory:
    print(car)

# ipdb.set_trace()

# Add method to update car availability
def mark_as_sold(self):
        self.available = False

# Add method to update car details
def update_details(self, make=None, model=None, year=None, price=None, mileage=None, color=None, available=None, car_type_name=None, car_type_description=None):
        if make:
            self.make = make
        if model:
            self.model = model
        if year:
            self.year = year
        if price:
            self.price = price
        if mileage:
            self.mileage = mileage
        if color:
            self.color = color
        if available is not None:
            self.available = available
        if car_type_name:
            self.car_type_name = car_type_name
        if car_type_description:
            self.car_type_description = car_type_description

# Add method to associate car with its type
def associate_car_type(self, car_type_name, car_type_description):
        self.car_type_name = car_type_name
        self.car_type_description = car_type_description

# Add method to disassociate car from its type
def disassociate_car_type(self):
        self.car_type_name = None
        self.car_type_description = None
