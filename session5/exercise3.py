#3a
empty_dict = {}

print(empty_dict)

#3b
empty_dict['pokemon'] = "Bulbasaur"
empty_dict['type'] = "grass"
empty_dict['level'] = 5

print(empty_dict)

#3c

empty_dict['moves'] = "vine whip", "razor leaf", "growl cut"

print(empty_dict)

#3d
empty_dict['level'] = 10

print(empty_dict)

#3e
count = 0
for values in empty_dict['moves']:
    #print(values)
    if 'growl cut' in values:
        print("Cut move exist!")
        count = count + 1
        break
if count == 0:
    print("Not found!")