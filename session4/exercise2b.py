def shopping_calculator(shopping_cost, discount_appicable):
    if ( discount_appicable == True):
        total_shopping_cost = shopping_cost * 0.9
        print(f'The total shopping cost is £{total_shopping_cost}')

    elif (shopping_cost >= 100 ):
        total_shopping_cost = shopping_cost * 0.95
        print(f'The total shopping cost is £{total_shopping_cost}')
    else:
        total_shopping_cost = shopping_cost
        print(f'The total shopping cost is £{total_shopping_cost}')

shopping_calculator(20, True)
shopping_calculator(50, False)
shopping_calculator(50, True)
shopping_calculator(15, False)
shopping_calculator(150, False)
shopping_calculator(150, True)