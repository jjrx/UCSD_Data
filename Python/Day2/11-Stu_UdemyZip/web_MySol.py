import os
import csv

titles = []
prices = []
subscriber_counts = []
reviews = []
course_lengths = []

csvpath = os.path.join("Resources", "web_starter.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        titles.append(row[1])
        prices.append(row[4])
        subscriber_counts.append(row[5])
        reviews.append(row[6])
        # .split(" ")[0] will remove "hours" so all that is left is number
        course_lengths.append(row[-2].split(" ")[0])

percent_subscribers = []
for x in range(len(reviews)):
    # rounds to 2 decimal places
    percent_subscribers.append(round(int(reviews[x])/int(subscriber_counts[x])*100,2))

classes = zip(titles, prices, subscriber_counts, reviews, percent_subscribers, course_lengths)

# save the output file path
output_file = os.path.join("Resources","web_starter_output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Titles", "Prices", "Subscriber Counts", "Reviews", "Percent Subscribers", "Course Lengths (Hours)"])
    writer.writerows(classes)
