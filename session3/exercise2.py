#2a and 2b and

shopping_cost = float(input('What is the total price of your shopping? '))
discount_applicable = input('Do you have a discount code? y/n ')

if (shopping_cost >= 20 and discount_applicable == 'y'):
    total_cost = shopping_cost * 0.9

elif (shopping_cost >= 100 and discount_applicable == 'n'):
    total_cost = shopping_cost * 0.95
else:
    total_cost = shopping_cost

print(f'The total collection cost is {total_cost}')

if total_cost >= 30:
    final_cost = total_cost
else:
    final_cost = total_cost + 5

print(f'Total cost with shipping is {final_cost}')



