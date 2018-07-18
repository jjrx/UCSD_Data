import os
import csv

# Path to collect data from the Resources folder
wrestlingCSV = os.path.join('Resources', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def getPercentages(wrestlerData):
    games_won = int(wrestlerData[1])
    games_lost = int(wrestlerData[2])
    games_drawn = int(wrestlerData[3])
    # Find the total number of matches wrestled
    total = games_won + games_lost + games_drawn
    # Find the percentage of matches won
    percent_won = (games_won/total) * 100
    # Find the percentage of matches lost
    percent_lost = (games_lost/total) * 100
    # Find the percentage of matches drawn
    percent_drawn = (games_drawn/total) * 100
    # if the loss % is over 50, the wrestler is "Jobber". Otherwise he is "Superstar"
    if percent_lost > 50:
        type_of_wrestler = "Jobber"
    else:
        type_of_wrestler = "Superstar"
    # Print out the wrestler's name and their percentage stats
    print(f"Stats for {wrestlerData[0]}")
    print("-----------------")
    print(f"Percent of games won: {percent_won}")
    print(f"Percent of games lost: {percent_lost}")
    print(f"Percent of games drawn: {percent_drawn}")
    print(f"{wrestlerData[0]} is a {type_of_wrestler}")

# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)
