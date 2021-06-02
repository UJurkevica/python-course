#1a

shirt_price = float(input('What is the price of the shirt?'))

shirt_in_budget = shirt_price <= 25.00
print(f'Shirt is available within budget: {shirt_in_budget}')

shirt_in_color = input('Is shirt yellow? (y/n)')
shirt_all = (shirt_in_budget == True) and (shirt_in_color == 'y')

#1b

print(f'Shirt is available within budget and correct color: {shirt_all}'.upper())