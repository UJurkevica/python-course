#3a

def split(a):
    return [char for char in a]

a = "question"

print(split(a))

#3b

list_in_lists = [[5,3,2], [1,3,2,1], [3,2,3], [10,1,5], [6,7,2]]
x = len(list_in_lists)
#index = 0

print(list(map(sum, list_in_lists)))
print(max(list(map(sum, list_in_lists))))

print(sum(list_in_lists[0]))
print(len(list_in_lists))

#while len(list_in_lists) <= x:

for item in list_in_lists:
    print(item)
    #sum(item)
    #print(item)
    #print(index)
    #index = index + 1

for i in range(len(list_in_lists)):
    print(i)
    
print(x)