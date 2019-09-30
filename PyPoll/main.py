# PyPoll Python Homework_03
import os
import csv
import numpy as np

# find the file #Working_csv is name in reference code
csvpathpoll = os.path.join("election_data.csv")

#open the file in this manner to only have it open while using
with open(csvpathpoll,newline="") as file_handler:

    #read the rows
    csvreader = csv.reader(file_handler,delimiter=',')
    print(csvreader)

    #read the header
    csv_header = next(csvreader)
    
    #name variables initialized
    total_votes = 0
    # candidates = []
    total_candidates = 0
    valid_candidates = []
    votes = [row[2] for row in csvreader]
    total_votes = int(len(votes))
    candidate_votes = {}
    
    #list of all names
    allnames = np.array(votes)
    candidates = np.unique(allnames)
    print(allnames)
   

    for i in candidates:
        candidate_votes[i] = 0

    for j in votes:
        candidate_votes[j] = candidate_votes[j]+1

    # Determine the winner of the election
    # set variable to hold winner votes

    winner_votes=0
    winner_name=""
    for key , value in candidate_votes.items():
        if value > winner_votes:
            winner_votes = value    
            winner_name = key
    
    # create a dictionary to hold candidate percentages
    candidate_ps = {}

    for k in candidates:
        candidate_ps[k] = '{:.3f}'.format((candidate_votes[k]/total_votes)*100)

    def printandwrite(results):
        print (results)

    printandwrite("----------------")
    printandwrite("Election Results")
    printandwrite("----------------")
    printandwrite(f'Total Votes: {total_votes}')
    printandwrite("----------------")
    for name in candidates:
        printandwrite(f'{name}: {candidate_ps[name]}% ({candidate_votes[name]})')
    printandwrite("----------------")
    printandwrite(f'Winner: {winner_name}')
    printandwrite("----------------")


    
    # #this loops through the csv row by row - do the work within this loop.
    # for row in csvreader:
    #     row.count = total_votes
    #     print(total_votes)
        
    #     candidates.append(row[2])
    #     # total_votes.sum(row[0])

    #     # this prints all the big data - don't do this!
    #     # print([candidates])
    #     # print(total_votes)
        
    #     # print(row)

    # #declare variables


    # #print list of candidates

    # #I think I need something for the list
    # percentage_by_candidate = 0
    # winner = 0

    # print(f"Election Results")
    # print(f"---------------------")
    # print(f"Total Votes: {total_votes}")
    # print(f"---------------------")
    # #I think this is incorrect
    # print(list[candidates])
    # print(f"---------------------")
    # print("Winner: {winner}")
    