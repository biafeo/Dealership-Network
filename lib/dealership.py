from __init__ import CURSOR, CONN

class Dealer:
    all = {}
    
    def __init__(self, id, title, location, phone_number, employees, inventory):
        self.id = id
        self.title = title
        self.location = location
        self.phone_number = phone_number
        self.employees = employees
        self.inventory = inventory
        

    def __str__(self):
        return f"Dealer Name: {self.title}\nLocation: {self.location}\nContact: {self.phone_number}\nEmployees: {self.employees}\nInventory: {self.inventory}"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Dealer instances """
        sql = """
            CREATE TABLE IF NOT EXISTS dealerships (
            id INTEGER PRIMARY KEY,
            title TEXT,
            location TEXT,
            phone_number TEXT,
            employees INTEGER,
            inventory INTEGER DEFAULT 0)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Dealer instances """
        sql = """
            DROP TABLE IF EXISTS dealerships;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the title, location, phone_number, and employees values of the current Dealer instance.
        Update object id attribute using the primary key value of new row. """
        sql = """
            INSERT INTO dealerships (title, location, phone_number, employees)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.title, self.location, self.phone_number, self.employees))
        CONN.commit()
        
        
    @classmethod
    def dealer_from_db(cls, dealer_row):
        return cls(dealer_row[0], dealer_row[1], dealer_row[2], dealer_row[3], dealer_row[4], dealer_row[5])
    
    @classmethod
    def find_by_id(cls, dealer_id):
        """Find a dealership by its ID"""
        sql = """
            SELECT * FROM dealerships WHERE id = ?
        """
        CURSOR.execute(sql, (dealer_id,))
        dealer_data = CURSOR.fetchone()
        if dealer_data:
            return cls.dealer_from_db(dealer_data)
        else:
            return None
   
 #inventory display the amount of cars in inventory cell
 
    
    @classmethod
    def dealership_from_db(cls, dealership_row):
        return cls(dealership_row[0], dealership_row[1], dealership_row[2], dealership_row[3], dealership_row[4], dealership_row[5])

    @classmethod
    def update_inventory(cls):
        """Update the inventory column in the dealerships table based on the count of cars associated with each dealership."""
        try:
            CURSOR.execute("""
                UPDATE dealerships 
                SET inventory = (
                    SELECT COUNT(*) 
                    FROM dealerships 
                    WHERE dealerships.dealership_id = dealerships.id
                )
            """)
            CONN.commit()
        except Exception as e:
            CONN.rollback()

    @classmethod
    def find_by_title(cls, title):
        data = CURSOR.execute("SELECT * FROM dealerships WHERE title = ?", (title,)).fetchone()
        if data:
            return cls.dealership_from_db(data)
    
    #display the cars in the inventory 
    @staticmethod
    def display_inventory(dealership_id):
        """Display the inventory of cars for a specific dealership"""
        sql = """
            SELECT * FROM cars WHERE dealership_id = ?
        """
        CURSOR.execute(sql, (dealership_id,))
        car_data = CURSOR.fetchall()

        return car_data
        
    
    

    @classmethod
    def get_all_dealers(cls):
        """Return a list of all Dealer objects"""
        sql = """
            SELECT * FROM dealerships
        """
        CURSOR.execute(sql)
        results = CURSOR.fetchall()

        dealers = []
        for result in results:
            dealer = cls(result[0], result[1], result[2], result[3], result[4], result [5])
            dealers.append(dealer)

        return dealers
    
    @classmethod
    def add_dealership(cls, title, location, phone_number, employees, inventory):
        CURSOR.execute("INSERT INTO dealerships (title, location, phone number, employees, inventory) VALUES (?, ?, ?, ?, ?)",
                    (title, location, phone_number, employees, inventory))
        CONN.commit() 
        new_dealership_id = CURSOR.lastrowid 
        return cls.dealership_from_db((new_dealership_id, title, location, phone_number, employees, inventory))
    
    @classmethod
    def delete_dealership(cls, title, location):
        CURSOR.execute("DELETE FROM dealerships WHERE title = ? AND location = ?", (title, location))
        CONN.commit()
        
        if CURSOR.rowcount > 0:
            print("Dealership deleted!")
        else:
            print("No dealerships found to delete")

    # @classmethod
    # def find_by_title(cls, title, location):
    #     data = CURSOR.execute("SELECT * FROM dealerships WHERE title = ?", (title, location)).fetchone()
    #     if data:
    #         return cls.dealer_from_db(data)
        

    def update(self, new_title, new_location, new_phone_number, new_employees, new_inventory):
            
        if new_title:
            self.title = new_title
        if new_location:
            self.location = new_location
        if new_phone_number:
            self.phone_number = new_phone_number
        if new_employees:
            self.employees = new_employees
        if new_inventory:
            self.inventory = new_inventory
    
        
        CURSOR.execute("UPDATE dealerships SET title = ?, location = ?, phone number = ?, employees = ?, inventory = ?, WHERE id = ?",
                    (self.title, self.location, self.phone_number, self.employees, self.inventory, self.id))
        CONN.commit()
        
        return self 
    
    @classmethod
    def sort_dealership_inventory_asc(cls):
        sort_dealership_asc = CURSOR.execute("SELECT * FROM dealerships ORDER BY dealerships.inventory ASC;").fetchall()
        return [cls.dealership_from_db(dealership_row) for dealership_row in sort_dealership_asc]

    @classmethod
    def sort_dealership_inventory_desc(cls):
        sort_inventory_desc =  CURSOR.execute("SELECT * FROM dealerships ORDER BY dealerships.inventory DESC;").fetchall()
        return [cls.dealership_from_db(dealership_row) for dealership_row in sort_inventory_desc]
        
    @classmethod
    def sort_dealership_employees_asc(cls):
        sort_employees_asc = CURSOR.execute("SELECT * FROM dealerships ORDER BY dealerships.employees ASC;").fetchall()
        return [cls.dealership_from_db(dealership_row) for dealership_row in sort_employees_asc]
    
    @classmethod
    def sort_dealership_employees_desc(cls):
        sort_employees_desc = CURSOR.execute("SELECT * FROM dealerships ORDER BY dealerships.employees DESC;").fetchall()
        return [cls.dealership_from_db(dealership_row) for dealership_row in sort_employees_desc]

    # @classmethod
    # def see_only_available_dealerships(cls):
    #     only_available = CURSOR.execute("SELECT * FROM dealerships WHERE available = 1;").fetchall()
    #     return [cls.dealership_from_db_from_db(dealership_row) for dealership_row in only_available]

    # @classmethod
    # def update_inventory(cls):
    #     """Update the inventory column of each dealership with the count of cars associated with it"""
    #     dealerships = CURSOR.execute("SELECT id FROM dealerships").fetchall()
    #     for dealership in dealerships:
    #         dealership_id = dealership[0]
    #         count_query = CURSOR.execute("SELECT COUNT(*) FROM cars WHERE dealership_id = ?", (dealership_id,))
    #         count = count_query.fetchone()[0]
    #         CURSOR.execute("UPDATE dealerships SET inventory = ? WHERE id = ?", (count, dealership_id))

    #     CONN.commit()
