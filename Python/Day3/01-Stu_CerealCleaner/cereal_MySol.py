import os
import csv

csvpath = os.path.join('Resources', 'cereal.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    print("The following cereal have >=5 g of fiber:")
    for row in csvreader:
        # if fiber is greater than or equal to 5, print out the cereal name
        if float(row[7]) >= 5:
            print(row[0])
