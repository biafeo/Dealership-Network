from car import Car
from tabulate import tabulate
from dealership import Dealer


def view_all_cars():
    print("View All Cars:")
    cars = Car.get_all()
    if cars:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Availability"]
        rows = []
        for car in cars:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Sold"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars found.")


def display_location():
    print("find the dealership:")
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    car = Car.find_by_make_and_model(make, model)
    
    if car:
        dealership_id = car.dealership_id  
        dealership = Dealer.find_by_id(dealership_id)
        if dealership:
            headers = ["Title", "Location", "Phone Number", "Employees", "Inventory"]
            row = [dealership.title, dealership.location, dealership.phone_number, dealership.employees, dealership.inventory]
            print(tabulate([row], headers=headers, tablefmt="grid"))
        else:
            print("No dealership found.")
    else:
        print("Car not found.")


        
def add_car():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = int(input("Enter car year: "))
    price = float(input("Enter car price: "))
    mileage = float(input("Enter car mileage: "))
    color = input("Enter color: ")
    car_type = input("Enter car type (gas or eletric): ")
    available = True 
    try:
        Car.add_car(make, model, year, price, mileage, color, car_type, available)
        print("Car added successfully!")
    except Exception as e:
        print("Error:", e)
        print("Failed to add car. Please try again.")
    
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
        new_car_type = input(f"Enter new car type [{car.car_type}]: ") 
        new_available = input(f"Enter availability (True or False): ")
        if new_available.lower() == "true":
            new_available = True
        elif new_available.lower() == "false":
            new_available = False
        else:
            new_available = car.available   
        new_dealership_id = input(f"Enter the new dealership id[{car.dealership_id}]:")
        
        update_car = car.update(new_make, new_model, new_year, new_price, new_mileage, new_color, new_car_type, new_available, new_dealership_id)
        if update_car:
            print("Car updated successfully!")
            Dealer.update_inventory()
        else: 
            print("Failed to update car")
    else:
        print("No car found with the given make and model.")
        
        
def delete_car():
    print("Delete Car:")
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    Car.delete_car(make, model)
    Dealer.update_inventory()
    
    

        

def view_cars_by_type(car_type):
    print("View Cars by Type:")
    filtered_cars = Car.view_cars_by_type(car_type)
    if filtered_cars:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Availability"]
        rows = []
        for car in filtered_cars:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Not Available"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars of this type found.")
                    
 
def sort_cars_price_asc():
    print("view cars by price ascending:")
    sort_price_asc = Car.sort_cars_price_asc()
    if sort_price_asc:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Availability"]
        rows = []
        for car in sort_price_asc:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Not Available"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars found.")
   
def sort_cars_price_des():
    print("view cars by price descending:")
    sort_price_desc = Car.sort_cars_price_des()
    if sort_price_desc:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Availability"]
        rows = []
        for car in sort_price_desc:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Not Available"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
            
    else:
        print("No cars found.")
            
       
            
def sort_cars_mileage_asc():
    print("view cars by mileage ascending:")
    sort_mileage_asc = Car.sort_cars_mileage_asc()
    if sort_mileage_asc:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type",  "Availability"]
        rows = []
        for car in sort_mileage_asc:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Not Available"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars found.")

  
def sort_cars_mileage_des():
    print("view cars by mileage descending:")
    sort_mileage_desc = Car.sort_cars_mileage_des()
    if sort_mileage_desc:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Availability"]
        rows = []
        for car in sort_mileage_desc:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Not Available"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars found.")




def see_only_available_cars():
    print("view cars that are available:")
    only_available = Car.see_only_available_cars()
    if only_available:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Availability"]
        rows = []
        for car in only_available:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Not Available"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars available")



def see_only_sold_cars():
    print("view cars that are sold:")
    only_sold = Car.see_only_sold_cars()
    if only_sold:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Availability"]
        rows = []
        for car in only_sold:
            availability = bool(car.available)
            availability_text = "Available" if availability else "Sold"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars sold")

    