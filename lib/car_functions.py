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
        
        #not working properly if left blank it delets the cell// ask morgan monday
def update_car():
    print("Update car:")
    make = input("Enter car make: ")
    model = input("Enter car model: ")

    CURSOR.execute("SELECT * FROM cars WHERE make = ? AND model = ?", (make, model))
    car = CURSOR.fetchone()

    if car:
        print("Fill in only the inputs that you want to update (leave blank to keep the same)")

        new_make = input(f"Enter new make [{car[0]}]: ") or car[0]
        new_model = input(f"Enter new model [{car[1]}]: ") or car[1]
        new_year = input(f"Enter new year [{car[2]}]: ") or car[2]
        new_price = input(f"Enter new price [{car[3]}]: ") or car[3]
        new_mileage = input(f"Enter new mileage [{car[4]}]: ") or car[4]
        new_color = input(f"Enter new color [{car[5]}]: ") or car[5]
        new_available = input(f"Enter availability (True or False) [{car[6]}]: ") or car[6]
        new_car_type = input(f"Enter new car type [{car[7]}]: ") or car[7]

        CURSOR.execute(
            "UPDATE cars SET make = ?, model = ?, year = ?, price = ?, mileage = ?, color = ?, available = ?, car_type = ? WHERE make = ? AND model = ?",
            (new_make, new_model, new_year, new_price, new_mileage, new_color, new_available, new_car_type, make, model))
        CONN.commit()

        if CURSOR.rowcount > 0:
            print("Car updated successfully!")
        else:
            print("No car found with the given make and model.")
    else:
        print("No car found with the given make and model.")
        


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
        
        
            
        # see bears lab to add more functionality 
        # maybe have a nested sort option
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

    