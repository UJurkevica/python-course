def my_maths_function(x, y, name):
    if name == 'add':
        print(x + y)

    elif name == 'substract':
        print(x - y)

    elif name == 'multiply':
        print(x * y)

    elif name == 'divide':
        print(x / y)

    else:
        print('Something went wrong!')

my_maths_function( 10, 5, 'add')
my_maths_function( 10, 2, 'substract')
my_maths_function( 6, 2, 'multiply')
my_maths_function( 1, 2, 'divide')
my_maths_function( 1, 2, 'hi')
my_maths_function( 1, 2, 5)
#if mathematical function is not recognised it will ignore the function
#as else option is introduced it prints the statement