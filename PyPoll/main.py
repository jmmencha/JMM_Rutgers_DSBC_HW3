# Rutgers DSBC - HW3 - Python - Jacob Menchak - PyPoll:

import os
import csv
import logging

# Import the CSV file:

# My CSV Path:
os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Temporarily hard-coding the CSV file path when error present:
#election_data_csv = 'C:/Users/jmenc/Documents/DSBC_Rutgers/03-Homework/Python/Instructions/PyPoll/Resources/election_data.csv'


# Variables:
votes_cast_count = 0
candidates_list = []
candidates_unique = []
khan_vote_count = 0
correy_vote_count = 0
li_vote_count = 0
otolley_vote_count = 0
khan_vote_percentage = 0
correy_vote_percentage = 0
li_vote_percentage = 0
otolley_vote_percentage = 1


# Open and read the "election_data.csv" CSV file, loop through each row in the file:
with open(election_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first:
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")


    # Find "the total number of votes cast":
    # Read through each row of data after the header.    
    # For reference, the total number of votes cast should be:  3,521,001
    for row in csv_reader:
        votes_cast_count += 1
        #print(row)
    #print(votes_cast_count)


    # Find "a complete list of candidates who received votes":
    # Create a list of ALL "candidate" values:
        candidate_string = str(row[2])
        # Add each "candidate" value from "candidate_string" (column C) to the end of the "candidates_list" list:
        candidates_list.append(candidate_string)
    #print(candidates_list)
    # Eliminate duplicate "candidate" values from the "candidates_list", and store unique candidate values in the "candidates_unique" list:
    # Iterate through all elements of the "candidates_list" list:
    for candidate_name in candidates_list:
        # If a unique candidate name is found, add it to the end of the "candidates_unique" list:
        if candidate_name not in candidates_unique:
            candidates_unique.append(candidate_name)
    #print(candidates_unique)


# Find "The total number of votes each candidate won":
# Count the number of times element, "Khan", appears in the list, "candidates_list":
khan_vote_count = candidates_list.count('Khan')
#print("Votes for Khan: " + str(khan_vote_count))

# Count the number of times element, "Correy", appears in the list, "candidates_list":
correy_vote_count = candidates_list.count('Correy')
#print("Votes for Correy: " + str(correy_vote_count))

# Count the number of times element, "Li", appears in the list, "candidates_list":
li_vote_count = candidates_list.count('Li')
#print("Votes for Li: " + str(li_vote_count))

# Count the number of times element, "O'Tooley", appears in the list, "candidates_list":
otooley_vote_count = candidates_list.count("O'Tooley")
#print("Votes for O'Tooley: " + str(otooley_vote_count))


# Find "the percentage of votes each candidate won":
#print(votes_cast_count)
# Percent of votes won by Khan:
khan_vote_percentage = khan_vote_count / votes_cast_count
#print(round(float(khan_vote_percentage * 100), 5))

# Percent of votes won by Correy:
correy_vote_percentage = correy_vote_count / votes_cast_count
#print(round(float(correy_vote_percentage * 100), 5))

# Percent of votes won by Li:
li_vote_percentage = li_vote_count / votes_cast_count
#print(round(float(li_vote_percentage * 100), 5))

# Percent of votes won by O'Tooley:
otooley_vote_percentage = otooley_vote_count / votes_cast_count
#print(round(float(otooley_vote_percentage * 100), 5))
 

# Logging:
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
# ***PLEASE_TAKE_NOTE***: The OUTPUT is being exported to a text file (log file) located at: C:\Users\CURRENT_USER
logger.addHandler(logging.FileHandler('./JMM_RutgersDSBC_HW3_Python_PyPoll_LogFileOutput.log', 'a'))
print = logger.info
print('If you can see this message, JMMs HW3 PyPoll Logger is exporting the HW3_PyPoll.py OUTPUT to this text file correctly :-)')
print('please note that this OUTPUT is being exported to a text file (log file) located at C_Users_CurrentUser')


# Print Statements / Output:
print("'''text \nElection Results \n-------------------------")
print(f"Total Votes: " + str(votes_cast_count))
print("-------------------------")
print(candidates_unique[0] + ": " + str(round(float(khan_vote_percentage * 100), 4)) + "00% " + "(" + str(khan_vote_count) + ")")
print(candidates_unique[1] + ": " + str(round(float(correy_vote_percentage * 100), 4)) + "00% " + "(" + str(correy_vote_count) + ")")
print(candidates_unique[2] + ": " + str(round(float(li_vote_percentage * 100), 4)) + "00% " + "(" + str(li_vote_count) + ")")
print(candidates_unique[3] + ": " + str(round(float(otooley_vote_percentage * 100), 4)) + "00% " + "(" + str(otooley_vote_count) + ")")
print("-------------------------")
#print("Winner: ")


# Find and print "the winner of the election based on popular vote":
if correy_vote_count > khan_vote_count:
    if correy_vote_count > li_vote_count:
        if correy_vote_count > otooley_vote_count:
            print("Winner: Correy")

if li_vote_count > khan_vote_count:
    if li_vote_count > correy_vote_count:
        if li_vote_count > otooley_vote_count:
            print("Winner: Li")

if otooley_vote_count > khan_vote_count:
    if otooley_vote_count > correy_vote_count:
        if otooley_vote_count > li_vote_count:
            print("Winner: O'Tooley")

if khan_vote_count > correy_vote_count:
    if khan_vote_count > li_vote_count:
        if khan_vote_count > otooley_vote_count:
            print("Winner: Khan")
else:
    #pass
    print("error in calculating winner")

print("-------------------------")
print("'''")


# Example Output:
# ```text
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# ```