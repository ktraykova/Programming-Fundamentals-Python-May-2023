n = int(input())

for _ in range(n):
    number = int(input())
    if number == 88:
        print("Hello")
    if number == 86:
        print("How are you?")
    if number != 86 and number != 88 and number < 88:
        print("GREAT!")
    if number > 88:
        print("Bye.")