#in this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration 
# isn't what it used to be.)
# You will be give a set of poll data called election_data.csv.
#  The dataset is composed of three columns: Voter ID, County, and Candidate.
#  Your task is to create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.
    #As an example, your analysis should look similar to the one below:
    #Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv
import os


output_file = "Poll_Results.txt"
#open the output file
file = open(output_file, 'w')

candidates = [2]
all_votes = []

def printResults():
    winner_count = 0
    total_votes = len(rowsArray) - 1
    winners_output = 0
    
    print('Election Results')
    print('----------------------------')
    print('Total Votes: ', total_votes)
    print('----------------------------')

    for can in candidates:
        candidate_count = all_votes.count(can)
        percentage_vote =  round((candidate_count / total_votes) * 100, 3)
        winners_output = winners_output + can + ': ' + str( percentage_vote) + '% (' + str(candidate_count) + ')' + '\n'
        print(can + ': ' + str( percentage_vote) + '% (' + str(candidate_count) + ')')

        if candidate_count > winner_count:
            winner_count = candidate_count
            winner = can

    print('----------------------------')
    print('Winner : ' + winner)
    print('----------------------------')

    file.write('Election Results\n')
    file.write('----------------------------\n')
    file.write("Total Votes: " + str(total_votes) + '\n')
    file.write('----------------------------\n')
    file.write(winners_output)
    file.write('----------------------------\n')
    file.write('Winner : ' + winner + '\n')
    file.write('----------------------------\n')

csvpath = os.path.join('/Users/mignonduplessis/Documents/BootCampRep/python_challenge/PyPoll/main.py/poll.py')
with open(csvpath, newline='') as csvfile:

    # create CSV reader 
    csvreader = csv.reader(csvfile, delimiter=',')

    # converts csvreader to list
    rowsArray = list(csvreader)
    newlist=[]
    # Print the contents of each row
    for i in rowsArray:
        # if candidate no in candidates array
        if [2] not in candidates:
            # add candidate to candidates array
           newlist=candidates.append([2])

        # add each candidate to all_votes array
        newlist=all_votes.append([2])

printResults()