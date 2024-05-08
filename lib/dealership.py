from __init__ import CURSOR, CONN
from car import Car

class Dealer:
    all = {}
    
    def __init__(self, id, title, location, phone_number, employees):
        self.id = id
        self.title = title
        self.location = location
        self.phone_number = phone_number
        self.employees = employees
        self.inventory = 0
        

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
        
 #inventory display the amount of cars in inventory cell
 
    @classmethod
    def update_inventory(cls):
        """Update the inventory column in the dealerships table based on the count of cars associated with each dealership."""
        try:
            CURSOR.execute("""
                UPDATE dealerships 
                SET inventory = (
                    SELECT COUNT(*) 
                    FROM cars 
                    WHERE cars.dealership_id = dealerships.id
                )
            """)
            CONN.commit()
        except Exception as e:
            CONN.rollback()
       
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
    def dealer_from_db(cls, dealer_row):
        return cls(dealer_row[1], dealer_row[2], dealer_row[3], dealer_row[4], dealer_row[5])

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
            dealer = cls(result[0], result[1], result[2], result[3], result[4])
            dealers.append(dealer)

        return dealers

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
