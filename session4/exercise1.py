#1a

def new_name(name):
    print(f'Hello {name}')

new_name('Una')
new_name('Laura')
new_name('Izzy')

#1b

def new_number(num):
    if (num % 2 == 0):
        print(True)
    else:
        print(False)


new_number(4)
new_number(13)

def check_even(num2):
    if num2 % 2 == 0:
        is_even = True
    else:
        is_even = False
    return is_even

num2 = int(input('Enter a number '))
is_even = check_even(num2)
print(f'Is {num2} even? {is_even}')