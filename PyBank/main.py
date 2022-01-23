import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
monthcount = []
total = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        monthcount.append(row[0])
        total.append(int(row[1]))
    for i in range(len(total)-1):
        change.append(total[i+1]-total[i])
greatest_increase = max(change)
greatest_decrease = min(change)
month_increase = change.index(max(change)) + 1
month_decrease = change.index(min(change)) + 1

print("Financial Analysis")
print("----------------------------")
print (f"Months: {len(monthcount)}")    
print (f"Total: ${sum(total)}")
print (f"Average Change: {round(sum(change)/len(change),2)}")
print (f"Greatest Increase in Profits: {monthcount[month_increase]} (${(str(greatest_increase))})")
print (f"Greatest Decrease in Profits: {monthcount[month_decrease]} (${(str(greatest_decrease))})")

f = open("analysis1.txt", mode = "w")
f.write("Financial Analysis")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write(f"Months: {len(monthcount)}")
f.write("\n")
f.write(f"Total: ${sum(total)}")
f.write("\n")
f.write(f"Average Change: {round(sum(change)/len(change),2)}")
f.write("\n")
f.write(f"Greatest Increase in Profits: {monthcount[month_increase]} (${(str(greatest_increase))})")
f.write("\n")
f.write(f"Greatest Decrease in Profits: {monthcount[month_decrease]} (${(str(greatest_decrease))})")
f.close()




