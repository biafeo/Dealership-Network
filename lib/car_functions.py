from dealership import Car
from __init__ import CURSOR, CONN
from tabulate import tabulate




def view_all_cars():
    print("View All Cars:")
    cars = Car.get_all()
    if cars:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Availability", "Car Type"]
        rows = []
        for car in cars:
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, "Available" if car.available else "Not Available", car.car_type]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars found.")

def add_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    price = float(input("Enter car price: "))
    mileage = float(input("Enter car mileage: "))
    color = input("Enter color: ")
    available = True 
    car_type = input("Enter car type (regular or electric): ")
    try:
        Car.add_car(make, model, year, price, mileage, color, available, car_type)
        print("Car added successfully!")
    except Exception:
       print("Enter valid car")


        
def delete_car():
    print("Delete Car:")
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    Car.delete_car(make, model)
    
    
def update_car():
    print("Update car:")
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    
    car = Car.find_by_make_and_model(make, model)
    
    
    if car:
        print("Fill in only the inputs that you want to update (leave blank to keep the same)")

        new_make = input(f"Enter new make [{car.make}]: ")
        new_model = input(f"Enter new model [{car.model}]: ")
        new_year = input(f"Enter new year [{car.year}]: ") 
        new_price = input(f"Enter new price [{car.price}]: ") 
        new_mileage = input(f"Enter new mileage [{car.mileage}]: ") 
        new_color = input(f"Enter new color [{car.color}]: ")
        new_available = input(f"Enter availability (True or False) [{car.available}]: ")
        new_car_type = input(f"Enter new car type [{car.car_type}]: ") 
        
        update_car = car.update(new_make, new_model, new_year, new_price, new_mileage, new_color, new_available, new_car_type)
        if update_car:
            print("Car updated successfully!")
        else: 
            print("Failed to update car")
    else:
        print("No car found with the given make and model.")


def view_cars_by_type(car_type):
    print("View Cars by Type:")
    filtered_cars = Car.view_cars_by_type(car_type)
    if filtered_cars:
        for car in filtered_cars:
            print(car)
    else:
        print("No cars of this type found.")

                    
 
def sort_cars_price_asc():
    print("view cars by price ascending:")
    CURSOR.execute("SELECT * FROM cars ORDER BY cars.price ASC;")
    results = CURSOR.fetchall()
    if results:
        for car in results:
            print(car)
    else:
        print("No cars found")
    
def sort_cars_price_des():
    print("view cars by price descending:")
    CURSOR.execute("SELECT * FROM cars ORDER BY cars.price DESC;")
    results= CURSOR.fetchall()
    if results:
        for car in results:
            print(car)
        else:
            print("No cars found")
            
            
def sort_cars_mileage_asc():
    print("view cars by mileage ascending:")
    CURSOR.execute("SELECT * FROM cars ORDER BY cars.mileage ASC;")
    results = CURSOR.fetchall()
    if results:
        for car in results:
            print(car)
    else:
        print("No cars found")
        
        
def sort_cars_mileage_des():
    print("view cars by mileage descending:")
    CURSOR.execute("SELECT * FROM cars ORDER BY cars.mileage DESC;")
    results= CURSOR.fetchall()
    if results:
        for car in results:
            print(car)
        else:
            print("No cars found")
    
    
    
    
def see_only_available_cars():
    print("view cars that are available:")
    CURSOR.execute("SELECT * FROM cars WHERE available = True;")
    results = CURSOR.fetchall()
    if len(results) == 0:
        print("no cars available")
    else: 
        for car in results:
            print(car)


def see_only_sold_cars():
    print("view cars that are sold:")
    CURSOR.execute("SELECT * FROM cars WHERE available = False;")
    results = CURSOR.fetchall()
    if len(results) == 0:
        print("no cars sold")
    else: 
        for car in results:
            print(car)

    