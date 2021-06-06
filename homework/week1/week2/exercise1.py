#1a
for num in range(0,11):
    if num % 3 == 0:
        continue
    else:
        print(f'number {num}')

#1b
def print_nums():
    for num in range(0,10):
        if num % 3 == 0:
            continue
        else:
            print(f'Number in function range {num}')

print_nums()

#1c
max_number = int(input('Enter positive maximum print range value '))

def print_nums():
    for num in range(max_number):
        if num % 3 == 0:
            continue
        else:
            print(f'Number in function range {num}')

print_nums()