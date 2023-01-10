# import modules
import os
import csv

# create list of candidates
candidates = []
votes = []
first_can = []
second_can = []
third_can = []

# set file path
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        votes.append(row[0])
    
        if row[2] not in candidates:
            candidates.append(row[2])

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    if row[2] == candidates[0]:
        first_can.append(row[0])
    elif row[2] == candidates[1]:
        second_can.append(row[0])
    else: row[2] == candidates[2]:
        third_can.append(row[0])
                   
votes_total = len(votes)
first_votes = len(first_can)
second_votes = len(second_can)
third_votes = len(third_can)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes_total))
print("-------------------------")
print(candidates[0] + ": " + str(first_votes/votes_total * 100) + "% (" + str(first_votes) + ")")
print(candidates[1] + ": " + str(second_votes/votes_total * 100) + "% (" + str(second_votes) + ")")
print(candidates[2] + ": " + str(third_votes/votes_total * 100) + "% (" + str(third_votes) + ")")


output_file = os.path.join('analysis', 'analysis.txt')

with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)
    