#3a

def split(a):
    return [char for char in a]

a = "question"

print(split(a))

#3b

list_in_lists = [[5,3,2], [1,3,2,1], [3,2,3], [10,1,5], [6,7,2]]

print(list(map(sum, list_in_lists)))
# print(max(list(map(sum, list_in_lists))))


def item_of_list():
    for item in list_in_lists:
        sum_of_list(item)
    return item


def sum_of_list(onelist):
    total = 0
    l = onelist
    for n in l:
        total = total + n
    #print(f'The list is {l} and the value is sum= {total}')
    if total == max(list(map(sum, list_in_lists))):
        print(f'The list with largest sum is list {l}, and sum= {total}')

item_of_list()