def shopping_calculator(shopping_cost, discount_appicable):
    if ( discount_appicable == 'y'):
        total_shopping_cost = shopping_cost * 0.9
        print(f'The total shopping cost is £{total_shopping_cost}')

    elif (shopping_cost >= 100 ):
        total_shopping_cost = shopping_cost * 0.95
        print(f'The total shopping cost is £{total_shopping_cost}')
    else:
        total_shopping_cost = shopping_cost
        print(f'The total shopping cost is £{total_shopping_cost}')

shopping_calculator(20, 'y')
shopping_calculator(50, 'n')
shopping_calculator(50, 'y')
shopping_calculator(15, 'n')
shopping_calculator(150, 'n')
shopping_calculator(150, 'y')