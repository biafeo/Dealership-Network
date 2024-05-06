import car_functions

def main_menu():
    while True:
        print("Welcome to the Dealership System!")
        print("Main Menu:")
        print("1. Add a car")
        print("2. Update car")
        print("3. Delete a car")
        print("4. View Cars")
      
      
        choice = input("Please enter your choice: ")

        if choice == "1":
            car_functions.add_car()
        elif choice == "2":
            car_functions.update_car()
        elif choice == "3":
            car_functions.delete_car()
        elif choice == "4":
            view_cars_menu()
        else:
            print("Invalid choice, please select option 1-6.")
            
            
            
def view_cars_menu():
    while True:
        print("\nView Cars Menu:")
        print("1. View All cars")
        print("2. view cars by type")
        print("3. view cars by price ascending")
        print("4. view cars by price descending")
        print("5. view cars by mileage ascending")
        print("6. view cars by mileage descending ")
        print("7. only available cars ")
        print("8. only sold cars")
        
        choice = input("please neter your choice: ")
        if choice == "1":
            car_functions.view_all_cars()
        elif choice == "2":
            car_type = input("Enter car type (eletric or gas): ")
            car_functions.view_cars_by_type(car_type)
        elif choice == "3":
            car_functions.sort_cars_price_asc()
        elif choice == "4":
            car_functions.sort_cars_price_des()
        elif choice == "5":
            car_functions.sort_cars_mileage_asc()
        elif choice == "6":
            car_functions.sort_cars_mileage_des()
        elif choice == "7":
            car_functions.see_only_available_cars()
        elif choice == "8":
            car_functions.see_only_sold_cars()
        else:
            print("Please enter a valid option:")

if __name__ == "__main__":
    main_menu()
