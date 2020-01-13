import csv
import os

#outputting results to a text file called Poll results
output_file = "Poll_Results.txt"
#open output file
file = open(output_file, 'w')

#set variables
candidates = []
votes = []

def printResults():
    winner_count = 0
    total_votes = len(rows) - 1
    winners_output = ''

    print('Election Results')
    print('----------------------------')
    print('Total Votes: ', total_votes)
    print('----------------------------')

    for x in candidates:
        candidate_count = votes.count(x)
        percentage = round((candidate_count / total_votes) * 100, 1)
        winners_output = winners_output + x + ': '  + str( percentage ) + '% (' + str(candidate_count) + ')' + '\n'
        print(x + ': ' + str( round((candidate_count / total_votes) * 100, 1) ) + '% (' + str(candidate_count) + ')')

        if candidate_count > winner_count:
            winner_count = candidate_count
            winner = x

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

csvpath = os.path.join('/Users/mignonduplessis/Documents/BootCampRep/python_challenge/PyPoll/Resources/election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # convert csv to list
    rows = list(csvreader)

    #get every row in dataset
    for i in range(1, len(rows)):
        # if candidate no in candidates list
        if rows[i][2] not in candidates:
            # add candidate to candidates list
            candidates.append(rows[i][2])

        # add each candidate to all_votes list
        votes.append(rows[i][2])

printResults()