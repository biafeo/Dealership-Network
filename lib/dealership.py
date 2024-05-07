from __init__ import CURSOR, CONN

class Dealer:
    all = {}
    
    def __init__(self, title, location, phone_number, employees):
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


    @classmethod
    def dealer_from_db(cls, dealer_row):
        return cls(dealer_row[1], dealer_row[2], dealer_row[3], dealer_row[4])

    @classmethod
    def get_all_dealers(cls):
        """Return a list containing a Dealer object per row in the dealerships table"""
        sql = """
            SELECT * FROM dealerships
        """

        dealer_data = CURSOR.execute(sql).fetchall()
        return [cls.dealer_from_db(dealer_row) for dealer_row in dealer_data]

    @classmethod
    def update_inventory(cls):
        """Update the inventory column of each dealership with the count of cars associated with it"""
        dealerships = CURSOR.execute("SELECT id FROM dealerships").fetchall()
        for dealership in dealerships:
            dealership_id = dealership[0]
            count_query = CURSOR.execute("SELECT COUNT(*) FROM cars WHERE dealership_id = ?", (dealership_id,))
            count = count_query.fetchone()[0]
            CURSOR.execute("UPDATE dealerships SET inventory = ? WHERE id = ?", (count, dealership_id))

        CONN.commit()