import os
import csv

user_movie = input("What movie are you looking for? ")

# set path for file
csvpath = os.path.join('Resources', 'netflix_ratings.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # csv_header = next(csvreader)
    # print(f"CSV header: {csv_header}")

    found = False
    for row in csvreader:
        if row[0] == user_movie:
            print(f"{row[0]} is rated {row[1]} with a rating of {row[-1]}.")
            found = True
            break # stop at first result to avoid duplication
    if(not found):
        print("Sorry, we could not find your movie!")
