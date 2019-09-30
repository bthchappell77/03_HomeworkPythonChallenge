# import module for reading files across operating systems and reading csv files easily
import os
import csv

# find the file
csvpathpoll = os.path.join("election_data.csv")

#open the file in this manner to only have it open while using
with open(csvpathpoll,newline="") as file_handler:

    #read the rows
    csvreader = csv.reader(file_handler,delimiter=',')
    print(csvreader)

    #read the header
    csv_header = next(csvreader)
    print(f'csv_header: {csv_header}')

    total_votes = 0
    candidates = []
    total_candidates = 0
    valid_candidates = []
    
    #this loops through the csv row by row - do the work within this loop.
    for row in csvreader:
        candidates.append(row[2])
        # total_votes.sum(row[0])
        print([candidates])
        # print(total_votes)
        
        # print(row)

    #declare variables


    #print list of candidates

    #I think I need something for the list
    percentage_by_candidate = 0
    winner = 0

    print(f"Election Results")
    print(f"---------------------")
    print(f"Total Votes: {total_votes}")
    print(f"---------------------")
    #I think this is incorrect
    print(list[candidates])
    print(f"---------------------")
    print("Winner: {winner}")
    