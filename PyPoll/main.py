# import modules
import os
import csv

# create list of candidates
candidates = []

# set file path
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter="'")

    csv_header = next(csvreader)

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            print(candidates)

output_file = os.path.join('analysis', 'analysis.txt')

with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)
    