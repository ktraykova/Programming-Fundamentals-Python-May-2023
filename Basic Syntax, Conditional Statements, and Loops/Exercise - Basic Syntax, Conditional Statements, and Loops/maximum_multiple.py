divisor = int(input())
boundary = int(input())
largest = 0

for largest in range(boundary, divisor, -1):
    if largest % divisor == 0:
        print(largest)
        break