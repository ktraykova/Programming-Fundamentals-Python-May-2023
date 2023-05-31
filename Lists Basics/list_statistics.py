number_of_lines = int(input())

positive_numbers = []
negative_numbers = []

positive_counter = 0
sum_negative = 0

for integers in range(number_of_lines):
    integer = int(input())

    if integer >= 0:
        positive_numbers.append(integer)
        positive_counter += 1
    else:
        negative_numbers.append(integer)
        sum_negative += integer

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {sum_negative}")