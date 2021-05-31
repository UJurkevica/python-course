#3a
floating_var = 8.98
integer_var = 4
string_var = 'Jam'

#3b
print(f'This item is an integer: {floating_var.is_integer()}')
#test if variable is integer
print(f'Ratio of this integer is: {integer_var.as_integer_ratio()}')
#it provides ratio for the variable (in this case for the integer)
print(f'Given variable begins with a letter J : {string_var.startswith("J")}')
#checks if variable begins with given value