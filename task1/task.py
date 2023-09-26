import csv

path = input()
line = int(input())
column = int(input())

result = []
with open(path, 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader: 
        result.append(row)

print(result[line][column])