import csv

with open( "example.csv","r" ) as file:
   reader = csv.reader(file, delimiter='-')

   headers = next(reader)

   for row in reader: 
    print(row)


