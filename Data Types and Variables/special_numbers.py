range_of_number = int(input())

for i in range(1, range_of_number + 1):
    number = str(i)
    is_special = False
    sum_of_numbers = 0
    for char in number:
        sum_of_numbers += int(char)
    if sum_of_numbers in [5, 7, 11]:
        is_special = True
    print(f"{i} -> {is_special}")