import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes +=1
        if row[2] == "Khan":
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li":
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
candidate_votes = [khan, correy, li, otooley]

zip_candidates = dict(zip(candidates, candidate_votes))
winner = max(zip_candidates, key=zip_candidates.get)
k_percentvote = (khan/total_votes)*100
c_percentvote = (correy/total_votes)*100
l_percentvote = (li/total_votes)*100
o_percentvote = (otooley/total_votes)*100

print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {k_percentvote:.3f}% ({khan})")
print(f"Correy: {c_percentvote:.3f}% ({correy})")
print(f"Li: {l_percentvote:.3f}% ({li})")
print(f"O'Tooley: {o_percentvote:.3f}% ({otooley})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

f = open("analysis2.txt", mode = "w",)
f.write("Election Results")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write(f"Total Votes: {total_votes}")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write(f"Khan: {k_percentvote:.3f}% ({khan})")
f.write("\n")
f.write(f"Correy: {c_percentvote:.3f}% ({correy})")
f.write("\n")
f.write(f"Li: {l_percentvote:.3f}% ({li})")
f.write("\n")
f.write(f"O'Tooley: {o_percentvote:.3f}% ({otooley})")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write(f"Winner: {winner}")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.close()


