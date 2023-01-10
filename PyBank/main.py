# import modules
import os
import csv

# create lists to store data
months = []
profits_losses = []
changes = []

# set file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# set variables for greatest increase and decrease values
increase = 0
decrease = 0

# read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    # store data in lists
    for row in csvreader:
        months.append(row[0])
        profits_losses.append(row[1])

        # take values for greatest increase and decrease
        if row[1] > increase:
            row = increase
            increase_month = row[0]
        if int(row[1]) < decrease:
            row = decrease
            decrease_month = row[0]

total_months = len(months)
total_profit = sum(profits_losses)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + total_months)
print("Total: $" + total_profit)
print("Greatest Increase in Profits: " + increase_month + "($" + increase + ")")
print("Greatest Decrease in Profits: " + decrease_month + "($" + decrease + ")")

output_file = os.path.join('analysis', 'analysis.txt')

with open(output_file, "w") as textfile:
    writer = csv.writer(textfile)

