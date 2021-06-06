def shopping_calculator(shopping_cost, discount_appicable):
    if ( discount_appicable == 'y'):
        total_shopping_cost = shopping_cost * 0.9
        #print(f' It is {total_shopping_cost}')

    elif (shopping_cost >= 100 ):
        total_shopping_cost = shopping_cost * 0.95
        #print(f'The total shopping cost is £{total_shopping_cost}')
    else:
        total_shopping_cost = shopping_cost
        #print(f'The total shopping cost is £{total_shopping_cost}')
    return total_shopping_cost


#shopping_calculator(20, 'y')
#shopping_calculator(50, 'n')
#shopping_calculator(50, 'y')
#shopping_calculator(15, 'n')
#shopping_calculator(150, 'n')
#shopping_calculator(150, 'y')

#add shipping costs and edit print statement above by adding return

def final_shopping_calculator(final_cost):
    total_shopping_cost = final_cost
    if total_shopping_cost >= 30:
        final_cost = total_shopping_cost
        print(f'Shopping final cost is {final_cost}')

    else:
        final_cost = total_shopping_cost + 5
        print(f'Final shopping cost is {final_cost}')


final_shopping_calculator(shopping_calculator(20, 'y'))
final_shopping_calculator(shopping_calculator(50, 'n'))
final_shopping_calculator(shopping_calculator(50, 'y'))
final_shopping_calculator(shopping_calculator(15, 'n'))
final_shopping_calculator(shopping_calculator(150, 'n'))
final_shopping_calculator(shopping_calculator(150, 'y'))