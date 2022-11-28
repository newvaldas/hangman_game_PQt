import csv

with open('countries.csv', 'r') as w:
    reader = csv.reader(w)
    data = list(reader)

print(type(data))