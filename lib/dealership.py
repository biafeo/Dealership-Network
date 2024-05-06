from __init__ import CURSOR, CONN

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



class Car:
    def __init__(self, make, model, year, price, mileage, color, available, car_type, id=None):
        # Initialize the Car object with provided attributes
        self.make = make  # Make of the car
        self.model = model  # Model of the car
        self.year = year  # Year of the car
        self.price = price  # Price of the car
        self.mileage = mileage  # Mileage of the car
        self.color = color  # Color of the car
        self.available = available  # Availability of the car
        self.car_type = car_type  # CarType object representing the type of the car
        self.id = id

    def __str__(self):
        # Return a string representation of the car
        availability = "Available" if self.available else "Not Available"
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nPrice: {self.price}\nMileage: {self.mileage}\nColor: {self.color}\nAvailability: {availability}\nCar Type: {self.car_type}"

    @classmethod
    def car_from_db(cls, car_row):
        return cls(car_row[1], car_row[2], car_row[3], car_row[4], car_row[5], car_row[6], car_row[7], car_row[8], car_row[0])
    
    
    #method to fetch all cars
    @classmethod
    def get_all(cls):
        car_data = CURSOR.execute("SELECT * FROM cars").fetchall()
        return [cls.car_from_db(car_row) for car_row in car_data]
    
    #method to add a car into DB
    @classmethod
    def add_car(cls, make, model, year, price, mileage, color, available, car_type):
        CURSOR.execute("INSERT INTO cars (make, model, year, price, mileage, color, available, car_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (make, model, year, price, mileage, color, available, car_type))
        CONN.commit() 
        new_car_id = CURSOR.lastrowid 
        return cls.car_from_db((new_car_id, make, model, year, price, mileage, color, available, car_type))
    
    
    #method to delete a car
    @classmethod
    def delete_car(cls, make, model):
        CURSOR.execute("DELETE FROM cars WHERE make = ? AND model = ?", (make, model))
        CONN.commit()
        
        if CURSOR.rowcount > 0:
            print("Car deleted sucessfully!")
        else:
            print("No car found to delete")
            
            
    #method to update car

    def update(self, new_make, new_model, new_year, new_price, new_mileage, new_color, new_available, new_car_type):
            
        if new_make:
            self.make = new_make
        if new_model:
            self.model = new_model
        if new_year:
            self.year = new_year
        if new_price:
            self.price = new_price 
        if new_mileage:
            self.mileage = new_mileage 
        if new_color:
            self.color = new_color 
        if new_available:
            self.available = new_available 
        if new_car_type:    
            self.car_type = new_car_type 
        
        CURSOR.execute("UPDATE cars SET make = ?, model = ?, year = ?, price = ?, mileage = ?, color = ?, available = ?, car_type = ? WHERE id = ?",
                    (self.make, self.model, self.year, self.price, self.mileage, self.color, self.available, self.car_type, self.id))
        CONN.commit()
        
        return self 
        
    @classmethod
    def find_by_make_and_model(cls, make, model):
        data = CURSOR.execute("SELECT * FROM cars WHERE make = ? AND model = ?", (make, model)).fetchone()
        if data:
            return cls.car_from_db(data)
        
        
    #method to view car by type

    @classmethod
    def view_cars_by_type(cls, car_type):
        filtered_cars = CURSOR.execute("SELECT * FROM cars WHERE car_type = ?", (car_type,)).fetchall()
        return [cls.car_from_db(car_row) for car_row in filtered_cars]
        


    
        

        