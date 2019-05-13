# This is just a comment
import os
import csv

# Path to collect data from the Resources folder
votesCSV = os.path.join('..', 'Resources', 'election_data.csv')

# Initialize Variables 
number_of_votes = 0
#* A complete list of candidates who received votes
unique_candidates = []

candidate_count = 0

final_candidate_name = []
final_candidate_count = []
final_candidate_pcnt = []

# Read in the CSV file
with open(votesCSV, 'r') as csvfile:

    # Split the data on commas
    #csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header line
    #header = next(csvreader)
    csvreader = list(csv.reader(csvfile, delimiter=','))
    csvreader.pop(0)
    number_of_votes = len(csvreader)
    
    # Loop through the data
    for candidates in csvreader:
    #     #candidates
         if  candidates[2] not in unique_candidates:
             unique_candidates.append(candidates[2])

    for candidate in unique_candidates:
        for all_candidates in csvreader:
            if candidate == all_candidates[2]:
                candidate_count += 1
        final_candidate_name.append(candidate)
        final_candidate_count.append(candidate_count)
        final_candidate_pcnt.append(round(candidate_count/number_of_votes * 100,2))
        candidate_count = 0 
        
#The greatest 
max_pcnt = max(final_candidate_pcnt)
max_pcnt_index = final_candidate_pcnt.index(max_pcnt)
winner = final_candidate_name[max_pcnt_index]

print('Election Results')
print('----------------------------')
print(f'Total Votes: {number_of_votes}')
print('----------------------------')
for i in range(len(final_candidate_name)):
    print(f'{final_candidate_name[i]}: {final_candidate_pcnt[i]} ({final_candidate_count[i]})')
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')

#write to a file

# Specify the file to write to
output_path = os.path.join("..", "Resources", "pyPollResults.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
outputFile = open(output_path,"w")

outputFile.write('Election Results\n')
outputFile.write('----------------------------\n')
outputFile.write(f'Total Votes: {number_of_votes}\n')
outputFile.write('----------------------------\n')
for i in range(len(final_candidate_name)):
    outputFile.write(f'{final_candidate_name[i]}: {final_candidate_pcnt[i]} ({final_candidate_count[i]})\n')
outputFile.write('----------------------------\n')
outputFile.write(f'Winner: {winner}\n')
outputFile.write('----------------------------\n')

outputFile.close() 
