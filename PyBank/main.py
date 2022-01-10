import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
monthcount = -1

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        monthcount += 1
    print("Months:", monthcount)

    


