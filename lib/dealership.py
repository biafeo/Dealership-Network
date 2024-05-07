from __init__ import CURSOR, CONN

class Dealer:
    def __init__(self, title, location, inventory, phone_number, employees):
        self.title = title
        self.location = location
        self.inventory = inventory
        self.phone_number = phone_number
        self.employees = employees
        
    def __str__(self):
        return f"Dealer Name: {self.title}\nLocation: {self.location}\nContact: {self.phone_number}\nEmployees: {self.employees}\n Inventory: {self.inventory}"

class Car:
    def __init__(self, id, make, model, year, price, mileage, color, available, car_type, dealership_id):
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage
        self.color = color
        self.available = available        
        self.car_type = car_type
        self.dealership_id = dealership_id

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nPrice: {self.price}\nMileage: {self.mileage}\nColor: {self.color}\nAvailability: {availability}\nCar Type: {self.car_type}"
    
    
    
    @classmethod
    def car_from_db(cls, car_row):
        return cls(car_row[0], car_row[1], car_row[2], car_row[3], car_row[4], car_row[5], car_row[6], car_row[7], car_row[8], car_row[9])
    
    
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
        if new_available is not None:
            new_available_int = 1 if new_available else 0
            self.available = new_available_int 
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

    #method to sort price by asc
    @classmethod
    def sort_cars_price_asc(cls):
        sort_price_asc = CURSOR.execute("SELECT * FROM cars ORDER BY price ASC;").fetchall()
        return [cls.car_from_db(car_row) for car_row in sort_price_asc]

  
    #method to sort price by desc
    @classmethod
    def sort_cars_price_des(cls):
        sort_price_desc =  CURSOR.execute("SELECT * FROM cars ORDER BY cars.price DESC;").fetchall()
        return [cls.car_from_db(car_row) for car_row in sort_price_desc]
        
    #method to sort mileage asc
    @classmethod
    def sort_cars_mileage_asc(cls):
        sort_mileage_asc = CURSOR.execute("SELECT * FROM cars ORDER BY cars.mileage ASC;").fetchall()
        return [cls.car_from_db(car_row) for car_row in sort_mileage_asc]
    
            
    #method sorty mileage desc
    @classmethod
    def sort_cars_mileage_des(cls):
        sort_mileage_desc = CURSOR.execute("SELECT * FROM cars ORDER BY cars.mileage DESC;").fetchall()
        return [cls.car_from_db(car_row) for car_row in sort_mileage_desc]

    
    
    #method only available cars
    @classmethod
    def see_only_available_cars(cls):
        only_available = CURSOR.execute("SELECT * FROM cars WHERE available = 1;").fetchall()
        return [cls.car_from_db(car_row) for car_row in only_available]

            
    #method only sold cars
    @classmethod
    def see_only_sold_cars(cls):
        only_sold =  CURSOR.execute("SELECT * FROM cars WHERE available = 0;").fetchall()
        return [cls.car_from_db(car_row) for car_row in only_sold]
