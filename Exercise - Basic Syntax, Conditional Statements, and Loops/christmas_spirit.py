quantity_of_decorations = int(input())
remaining_days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

total_cost = 0
total_spirit = 0

for days in range(1, remaining_days+1):
    if days % 11 == 0:
        quantity_of_decorations += 2
    if days % 2 == 0:
        total_cost += ornament_set * quantity_of_decorations
        total_spirit += 5
    if days % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * quantity_of_decorations
        total_spirit += 13
    if days % 5 == 0:
        total_cost += tree_lights * quantity_of_decorations
        total_spirit += 17
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights
if remaining_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")





