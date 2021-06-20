import csv

with open('session7/pokemon.csv', 'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['name', 'age'])
    csvwriter.writerows([['sally', '20'], ['tpyin', '32'], ['yussra', '63']])

with open('session7/pokemon.csv', 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        #print(row)
        print(row[0])