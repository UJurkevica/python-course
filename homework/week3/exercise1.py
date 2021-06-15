#1a

my_list = ["Amy", 1, "Beth", "Charlie", 6, "Daisy", 7, 2]

print(my_list)

#1b

my_list[2] = "Sandy"
print(my_list)

#1c
new_list =[]

for item in my_list:
    if type(item) == int:
        #print(type(item))
        item = (item)** 2
        #print(item)
    else:
        item = item
    
    print(item)
    new_list.append(item)

print(new_list)

#1d
count = 0

for val in new_list:
    if type(val) == int:
        if val >= 5:
            count = count + 1

        else:
            count = count

print(f'In given list {count} numbers are bigger than 5')