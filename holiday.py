# Holiday calculator to calculate hotel cost, plane cost, and car rental
# Welcome message and start selection 
def holiday_cost_calculator():
    print("Welcome to my holiday cost calculator\n")
    
    while True:
        menu_selection = input("\nAre you ready to choose your holiday? (Y or N): ")
        if menu_selection.upper() == 'Y':
            city_nights()
            break
        elif menu_selection.upper() == 'N':
            print("Thank you for visiting, please come again! Goodbye!")
            return
        else:
            print("Invalid selection! Please enter Y or N.")

# Define a function for user selection for city, nights, rental choice
# display user selection choice of city and price value
def city_nights():
    print('''             
           CITY            PRICE
      1 : Barcelona    : £ 250pp
      2 : Brno         : £ 180pp
      3 : Budapest     : £ 150pp
      4 : Coppenhagen  : £ 304pp
      5 : Milan        : £ 340pp''')

    # User inputs for city flight, number of nights, and car rental choice selection
    # Try/Except - error handling
    while True:
        try:
            city_flight = int(input("\nPlease chose your destination and enter the relevant number: "))
            break
        except ValueError:
            print("Invalid selection! Please enter a number!")

    while True:
        try:
            num_nights = int(input("\nHow many nights would you like to stay? "))
            break
        except ValueError:
            print("Invalid selection! Please enter a number!")

    while True:
        car_rental_menu = input("\nWould you like car rental? (Y or N): ")
        if car_rental_menu.upper() == "Y" or car_rental_menu.upper() == "N":
            break
        else:
            print("Invalid input. Please enter Y or N.")

    if car_rental_menu.upper() == "Y":
        while True:
            try:
                car_rental_duration = int(input("\nPlease enter the duration for car rental: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    #Hotel options
    print('''
      1: Standard:             £90 per night
      2: Bed and Breakfast:   £110 per night
      3: Half board:          £165 per night
      4: All inclusive:       £210 per night
     ''')
    
    while True:
        try:
            hotel_choice = int(input("\nPlease chose from the hotel options above: "))
            if hotel_choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid selection! Please enter a option from the selection above!")
        except ValueError:
            print("Invalid selection! Please enter a number!")

    #Hotel choices
    hotel_choice_dict = {
        1: "Standard",
        2: "Bed and Breakfast",
        3: "Half board",
        4: "All inclusive"
    }
    hotel_type = hotel_choice_dict[hotel_choice]

   #Cost of hotel choices
    hotel_type_cost = {
        "Standard": 90,
        "Bed and Breakfast": 110,
        "Half board": 165,
        "All inclusive": 210,
    }[hotel_type]

    #Flight choices
    city_flight_dict = {
        1: "Barcelona",
        2: "Brno",
        3: "Budapest",
        4: "Coppenhagen",
        5: "Milan",
    }

    #Flight costs
    city_flight_cost = {
        "Barcelona": 250,
        "Brno": 180,
        "Budapest": 150,
        "Coppenhagen": 304,
        "Milan": 340,
    }[city_flight_dict[city_flight]]
    print(f"\nLocation: {city_flight_dict[city_flight]}")

    total_hotel_cost = hotel_cost(hotel_type_cost, num_nights, hotel_type)
    total_flight_cost = plane_cost(city_flight_cost)
    total_car_rental_cost = 0

    if car_rental_menu.upper() == "Y":
        total_car_rental_cost = car_rental(car_rental_duration)

    total_holiday_cost(total_hotel_cost, total_flight_cost, total_car_rental_cost)


def hotel_cost(hotel_type_cost, num_nights, hotel_type):
    total_hotel_cost = hotel_type_cost * num_nights
    print(f"\nHotel type: {hotel_type}\nHotel price: £{hotel_type_cost}\nNumber of nights: {num_nights}\nHotel cost: £{total_hotel_cost}\n")
    return total_hotel_cost


def plane_cost(city_flight_cost):
    total_flight_cost = city_flight_cost
    print(f"Total flight cost: £{total_flight_cost} return")
    return total_flight_cost


# Return car_rental_cost for final pricing 
def car_rental(car_rental_duration):
    car_rental_cost = 25.50 * car_rental_duration
    print(f"\nPrice per day: £25.50\nDuration: {car_rental_duration} days \nCar rental cost: £{car_rental_cost}")
    return car_rental_cost

# Final function to calculate all cost
def total_holiday_cost(total_hotel_cost, total_flight_cost, total_car_rental_cost): 
    total_cost_of_holiday = total_hotel_cost + total_flight_cost + total_car_rental_cost
    print(f"\nTotal holiday cost: £{total_cost_of_holiday}\n")

holiday_cost_calculator()

# Reload function
reload_choice = input("Would you like to reload this calculator? (Y/N): ").upper()
if reload_choice == 'Y':
    city_nights()
else:
    print("Thanks for using my holiday calculator! Hope to see you again!")
    quit()
