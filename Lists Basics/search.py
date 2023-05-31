number_of_lines = int(input())
special_word = input()

list_of_tasks = []
list_of_python_tasks = []

for strings in range(number_of_lines):
    string = input()

    list_of_tasks.append(string)

    if special_word in string:
        list_of_python_tasks.append(string)

print(list_of_tasks)
print(list_of_python_tasks)