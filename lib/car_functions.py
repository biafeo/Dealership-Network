from dealership import Car
from __init__ import CURSOR, CONN


cars = []

def add_car(car):
    
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    price = float(input("Enter car price: "))
    mileage = float(input("Enter car mileage: "))
    car_type = input("Enter car type (regular or electric): ")
    
    
    CURSOR.execute("INSERT INTO cars VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                   (car.make, car.model, car.year, car.price, car.mileage, car.color, car.available, car.car_type))    
    
    print("Add a car")
 
    

    # Create a Car object
    car = Car(make, model, year, price, mileage, "", True, car_type)
    cars.append(car)  # Add the car to the list
    print("Car added successfully!")


def view_cars_by_type():
    print("View Cars by Type:")
    car_type = input("Enter car type (regular or electric): ").lower()
    filtered_cars = [car for car in cars if car.car_type.lower() == car_type]
    if filtered_cars:
        for car in filtered_cars:
            print(car)
    else:
        print("No cars of this type found.")

def view_cars_by_price():
    print("View Cars by Price:")
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    filtered_cars = [car for car in cars if min_price <= car.price <= max_price]
    if filtered_cars:
        for car in filtered_cars:
            print(car)
    else:
        print("No cars found within this price range.")

def view_cars_by_mileage():
    print("View Cars by Mileage:")
    min_mileage = float(input("Enter minimum mileage: "))
    max_mileage = float(input("Enter maximum mileage: "))
    filtered_cars = [car for car in cars if min_mileage <= car.mileage <= max_mileage]
    if filtered_cars:
        for car in filtered_cars:
            print(car)
    else:
        print("No cars found within this mileage range.")
        
    