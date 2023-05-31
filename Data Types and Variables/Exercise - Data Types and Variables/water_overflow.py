number_of_lines = int(input())
tank_capacity = 255
total_water = 0

for water in range(number_of_lines):
    liters_of_water = int(input())

    if liters_of_water > tank_capacity:
        print("Insufficient capacity!")
        continue

    tank_capacity -= liters_of_water
    total_water += liters_of_water

print(total_water)
