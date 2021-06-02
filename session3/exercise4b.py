counter = 0
total_sum = 0
while counter <= 500:
    if (counter % 3 == 0):
        total_sum = total_sum + counter
    counter = counter + 1
    print(f'Sum {total_sum}')
    print(f'Counter: {counter} ')

print(f'The sum of all numbers divisible by three between 1 and 500 is {total_sum}')