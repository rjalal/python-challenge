import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('..', 'Resources', 'budget_data.csv')

# Initialize Variables 
number_of_months = 0
total_amount = 0 
# to calculate the average change
changes = []
change = 0 
current_value = 0 
# to get the greatest increase and decrease per month
dates = []


# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header line
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        #count the number of rows to get the total number of months. 
        number_of_months += 1 
        #total amount
        total_amount += int(row[1])
        #average change 
        change = int(row[1]) - current_value
        changes.append(change)
        #add the date to another list 
        dates.append(row[0])
        current_value = int(row[1])
    changes.pop(0)
    dates.pop(0)

#The greatest increase in profits
max_increase = max(changes)
max_increase_idx = changes.index(max_increase)

#The greatest decrease in profits
max_decrease = min(changes)
max_decrease_idx = changes.index(max_decrease)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {number_of_months}')
print(f'Total: {total_amount}')
print(f'Average  Change: {sum(changes)/len(changes)}')
print(f'Greatest Increase in Profits: {dates[max_increase_idx]} ({max_increase})')
print(f'Greatest Decrease in Profits: {dates[max_decrease_idx]} ({max_decrease})')

#write to a file

# Specify the file to write to
output_path = os.path.join("..", "Resources", "pyBankResults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
outputFile = open(output_path,"w")
outputFile.write('Financial Analysis\n')
outputFile.write('----------------------------\n')
outputFile.write(f'Total Months: {number_of_months}\n')
outputFile.write(f'Total: {total_amount}\n')
outputFile.write(f'Average  Change: {sum(changes)/len(changes)}\n')
outputFile.write(f'Greatest Increase in Profits: {dates[max_increase_idx]} ({max_increase})\n')
outputFile.write(f'Greatest Decrease in Profits: {dates[max_decrease_idx]} ({max_decrease})\n')

outputFile.close() 