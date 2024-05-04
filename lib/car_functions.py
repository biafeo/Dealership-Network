from dealership import Car
from __init__ import CURSOR, CONN


cars = []

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
       CURSOR.execute("INSERT INTO cars (make, model, year, price, mileage, color, available, car_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                      (make, model, year, price, mileage, color, available, car_type))
       CONN.commit()
       print("Car added successfully!")
    except Exception:
       print("Enter valid car")

    car = Car(make, model, year, price, mileage, color, available, car_type)
    cars.append(car)  

    

def view_cars_by_type():
    print("View Cars by Type:")
    car_type = input("Enter car type (regular or electric): ").lower()
    CURSOR.execute("SELECT * FROM cars WHERE car_type = ?", (car_type,))
    filtered_cars = CURSOR.fetchall()
    if filtered_cars:
        for car in filtered_cars:
            print(car)
    else:
        print("No cars of this type found.")

def view_cars_by_price():
    print("View Cars by Price:")
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    CURSOR.execute("SELECT * FROM cars WHERE price BETWEEN ? AND ?", (min_price, max_price))
    filtered_cars = CURSOR.fetchall()
    if filtered_cars:
        for car in filtered_cars:
            print(car)
    else:
        print("No cars found within this price range.")

def view_cars_by_mileage():
    print("View Cars by Mileage:")
    min_mileage = float(input("Enter minimum mileage: "))
    max_mileage = float(input("Enter maximum mileage: "))
    CURSOR.execute("SELECT * FROM cars WHERE mileage BETWEEN ? AND ?", (min_mileage, max_mileage))
    filtered_cars = CURSOR.fetchall()
    if filtered_cars:
        for car in filtered_cars:
            print(car)
    else:
        print("No cars found within this mileage range.")
        
def delete_car():
    print("Delete Car:")
    make = input("Enter car make: ")
    model = input("Enter car model: ")

    CURSOR.execute("DELETE FROM cars WHERE make = ? AND model = ?", (make, model))
    CONN.commit()

    if CURSOR.rowcount > 0:
        print("Car deleted successfully!")
    else:
        print("No car found with the given make and model.")
        
        
        
def update_car():
        
        # see bears lab to add more functionality 
        # maybe have a nested sort option
def sort_cars_price_asc():
    pass
def sort_cars_price_des():
    pass
def sort_cars_mileage_asc():
    pass
def sort_cars_mileage_des():
    pass
def see_only_available_cars():
    pass
def see_only_sold_cars():
    pass