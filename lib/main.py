# import argparse

# def main():
#     parser = argparse.ArgumentParser(description='A basic CLI application')
#     parser.add_argument('-g', '--greet', help='Greet the user')
#     args = parser.parse_args()

#     if args.greet:
#         print('Hello, {}!'.format(args.greet))
#     else:
#         print('Hello!')

# if __name__ == "__main__":
#     main()
import car_functions
import dealership

def main_menu():
    while True:
        print("Welcome to the Dealership System!")
        print("Main Menu:")
        print("1. Add a car")
        print("2. View Cars by Type")
        print("3. View Cars By Price")
        print("4. View Cars by Mileage")
        print("5. Manage Dealership Information")
      
        choice = input("Please enter your choice: ")

        if choice == "1":
            car_functions.add_car()
        elif choice == "2":
            car_functions.view_cars_by_type()
        elif choice == "3":
            car_functions.view_cars_by_price()
        elif choice == "4":
            car_functions.view_cars_by_mileage()
        elif choice == "5":
        #call function for the dealership // 
        # here we have to explore more if we are having the employees info
        #also we can create extra options in the main menu for the dealership 
            pass
        else:
            print("Invalid choice, please select option 1-6.")

if __name__ == "__main__":
    main_menu()

