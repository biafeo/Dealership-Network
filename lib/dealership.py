class Dealer:
    def __init__(self, name, location, contact, employees):
        # Initialize the Dealer object with provided attributes
        self.name = name  # Name of the dealer
        self.location = location  # Location of the dealer
        self.contact = contact  # Contact information of the dealer
        self.employees = employees  # Number of employees at the dealer

    def __str__(self):
        # Return a string representation of the dealer
        return f"Dealer Name: {self.name}\nLocation: {self.location}\nContact: {self.contact}\nEmployees: {self.employees}"


class CarType:
    def __init__(self, name, description):
        # Initialize the CarType object with provided attributes
        self.name = name  # Name of the car type
        self.description = description  # Description of the car type

    def __str__(self):
        # Return a string representation of the car type
        return f"Car Type: {self.name}\nDescription: {self.description}"


class Car:
    def __init__(self, make, model, year, price, mileage, color, available, car_type):
        # Initialize the Car object with provided attributes
        self.make = make  # Make of the car
        self.model = model  # Model of the car
        self.year = year  # Year of the car
        self.price = price  # Price of the car
        self.mileage = mileage  # Mileage of the car
        self.color = color  # Color of the car
        self.available = available  # Availability of the car
        self.car_type = car_type  # CarType object representing the type of the car

    def __str__(self):
        # Return a string representation of the car
        availability = "Available" if self.available else "Not Available"
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nPrice: {self.price}\nMileage: {self.mileage}\nColor: {self.color}\nAvailability: {availability}\nCar Type: {self.car_type}"


# Mock Data for testing the classes
dealer = Dealer("ABC Motors", "123 Main St", "123-456-7890", 10)  # Creating a Dealer object
car_type = CarType("Electric", "Electric cars use electricity for propulsion")  # Creating a CarType object
car = Car("Tesla", "Model S", 2022, 80000, 5000, "Red", True, car_type)  # Creating a Car object

# Printing the string representations of the objects
print(dealer)  # Printing dealer info
print(car_type)  # Printing car type info
print(car)  # Printing car info
