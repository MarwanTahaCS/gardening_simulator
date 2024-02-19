plants_conditions = [["Rose", 0, 10, 0, 5],
                    ["sunflower", 1, 20, 1, 10],
                    ["Orchid", 0, 10, 1, 15]]

print("Answer questions below regarding the weather today")
is_sun = input("Is it (enter [0 for \"sunny\"] / [1 for \"cloudy\"])?")
while not is_sun.isdigit() or int(is_sun) not in [0, 1]:
    print("Invalid input. Enter 0 for sunny or 1 for cloudy.")
    is_sun = input("Is it (enter [0 for \"sunny\"] / [1 for \"cloudy\"])?")
is_sun = int(is_sun)
precipitation_number = input("What is the precipitation number?")
while not precipitation_number.isdigit() or int(precipitation_number) < 0:
    print("Invalid input. Enter a non-negative number.")
    precipitation_number = input("What is the precipitation number?")
precipitation_number = int(precipitation_number)
is_wind = input("Is it windy (enter [0 for \"no\"] / [1 for \"yes\"])?")
while not is_wind.isdigit() or int(is_wind) not in [0, 1]:
    print("Invalid input. Enter 0 for no or 1 for yes.")
    is_wind = input("Is it windy (enter [0 for \"no\"] / [1 for \"yes\"])?")
is_wind = int(is_wind)

for plant in plants_conditions:
    if plant[1] == is_sun and plant[2] == precipitation_number and plant[3] == is_wind:
        print(plant[0])

snow_amount = int(input("how much snow?"))

for plant in plants_conditions:
    if  snow_amount >= plant[4]:
        print(f"{plant[0]} is dead due to the snow")