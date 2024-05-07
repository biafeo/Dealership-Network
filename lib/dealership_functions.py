from dealership import Dealer
from tabulate import tabulate

def view_all_dealerships():
    print("View All Dealerships:")
    dealership = Dealer.get_all()
    if dealership:
        headers = ["Title", "Location", "Inventory", "Phone Number", "Employees"]
        rows = []
        for dealership in dealership:
            availability = bool(dealership.open)
            open_text = "Open" if availability else "Closed"
            row = [dealership.title, dealership.location, dealership.inventory, dealership.phone_number, dealership.employees, open_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No dealership found.")

def add_dealership():
    title = input("Enter car make: ")
    location = input("Enter car model: ")
    inventory = int(input("Enter car year: "))
    phone_number = float(input("Enter car price: "))
    employees = float(input("Enter car mileage: "))
    open = True 
    try:
        Dealer.add_dealership(title, location, inventory, phone_number, employees, open)
        print("Dealership has added!")
    except Exception as e:
        print("Error:", e)
        print("Please try again. Failed to add dealership.")

def delete_dealership():
    print("Delete Dealership:")
    title = input("Enter name of the dealership: ")
    location = input("Enter dealership location: ")
    Dealer.delete_dealership(title, location)

def update_dealership():
    print("Update Dealership:")
    title = input("Enter name of the dealership: ")
    location = input("Enter dealership location: ")
    
    dealership = Dealer.find_by_title_and_location(title, location)
    
    
    if dealership:
        print("Enter each of the inputs in order to update")

        new_title = input(f"Enter new title [{dealership.title}]: ")
        new_location = input(f"Enter new location [{dealership.location}]: ")
        new_inventory = input(f"Enter new inventory count [{dealership.inventory}]: ") 
        new_phone_number = input(f"Enter new phone number [{dealership.phone_number}]: ") 
        new_employees = input(f"Enter new employee count [{dealership.employees}]: ") 
        new_open = input(f"Enter availability (True or False): ")
        if new_open.lower() == "true":
            new_open = True
        elif new_open.lower() == "false":
            new_open = False
        else:
            new_open = dealership.open
        
        update_dealership = dealership.update(new_title, new_location, new_inventory, new_phone_number, new_employees, new_open)
        if update_dealership:
            print("Dealership updated successfully!")
        else: 
            print("Failed to update dealership")
    else:
        print("No dealership found.")

def see_only_open_dealerships():
    print("View dealerships that are open:")
    only_open = Dealer.see_only_open_dealerships()
    if only_open:
        headers = ["Title", "Location", "Inventory", "Phone Number", "Employees", "Open"]
        rows = []
        for dealership in only_open:
            open = bool(dealership.open)
            open_text = "Open" if open else "Closed"
            row = [dealership.title, dealership.location, dealership.inventory, dealership.phone_number, dealership.employees, open_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No dealerships available")

    



