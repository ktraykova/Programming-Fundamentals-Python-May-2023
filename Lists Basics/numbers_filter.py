number_of_lines = int(input())

numbers = []
filtered_numbers = []

for num in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)
elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)
elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)

print(filtered_numbers)




