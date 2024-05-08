
import dealership_functions
import car_functions


def main_menu():
    
    while True:
        print("=" * 50)
        print("Welcome to the Dealership System!")
        print("=" * 50)
        print("Main Menu:")
        print("1. Add a car")
        print("2. Update car")
        print("3. Delete a car")
        print("4. View Cars")
        print("5. Dealers Menu")
        print("6. Exit")
      
      
        choice = input("Please enter your choice: ")

        if choice == "1":
            car_functions.add_car()
        elif choice == "2":
            car_functions.update_car()
        elif choice == "3":
            car_functions.delete_car()
        elif choice == "4":
            view_cars_menu()
        elif choice == "5":
            dealership_menu()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please select an option:")

                
            
            
def view_cars_menu():
    while True:
        print("=" * 50)
        print("View Cars Menu:")
        print("=" * 50)
        print("1. View All cars")
        print("2. View Car location")
        print("3. View cars by type")
        print("4. View cars by price ascending")
        print("5. View cars by price descending")
        print("6. View cars by mileage ascending")
        print("7. View cars by mileage descending ")
        print("8. Only available cars ")
        print("9. Only sold cars")
        print("10. Back to main menu")
        
        choice = input("Please enter your choice: ")
        if choice == "1":
            car_functions.view_all_cars()
        elif choice == "2":
            car_functions.display_location()
        elif choice == "3":
            car_type = input("Enter car type (Electric or Gas): ")
            car_functions.view_cars_by_type(car_type)
        elif choice == "4":
            car_functions.sort_cars_price_asc()
        elif choice == "5":
            car_functions.sort_cars_price_des()
        elif choice == "6":
            car_functions.sort_cars_mileage_asc()
        elif choice == "7":
            car_functions.sort_cars_mileage_des()
        elif choice == "8":
            car_functions.see_only_available_cars()
        elif choice == "9":
            car_functions.see_only_sold_cars()
        elif choice == "10":
            break
        else:
            print("Please enter a valid option:")
            
            
def dealership_menu():
    while True:
        print("=" * 50)
        print("View Dealers Menu:")
        print("=" * 50)
        print("1. View all Dealerships")
        print("2. Update Dealerships data")
        print("3. View Dealerships by inventory count ascending")
        print("4. View Dealerships by inventory count descending")
        print("5. View Dealerships by employee count ascending")
        print("6. View Dealerships by employee count descending ")
        print("7. Back to main menu")
        
        choice = input("Please enter your choice: ")
        if choice == "1":
            dealership_functions.view_all_dealerships()
        elif choice == "2":
            dealership_functions.update_dealership()
        elif choice == "3":
            dealership_functions.sort_dealership_inventory_asc()
        elif choice == "4":
            dealership_functions.sort_dealership_inventory_desc()
        elif choice == "5":
            dealership_functions.sort_dealership_employees_asc()
        elif choice == "6":
            dealership_functions.sort_dealership_employees_desc()
        elif choice == "7":
            break
        else:
            print("Please enter a valid option:")
            
if __name__ == "__main__":
    main_menu()