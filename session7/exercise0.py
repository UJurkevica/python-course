import csv

file = open('session7/groceries.txt', 'r')
print(file.read())
file.close()


with open('session7/groceries.txt') as file:
    print('First line: ')
    print(file.readline())
    print(('Second line: '))
    print(file.readline())

with open('session7/groceries.txt') as file:
    print(file.readlines())

with open('session7/new-file.txt', 'w') as file:
    file.write(("Adding some more contents"))

with open('session7/new-file.txt', 'a') as file:
    file.write(("\nAdding some more contents to the end of the file\n"))

with open('session7/new-file.txt', 'a') as file:
    file.writelines(('item1\n', 'item2\n', 'item3\n'))
