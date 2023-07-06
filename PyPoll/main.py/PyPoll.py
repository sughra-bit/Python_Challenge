# Import modules os and csv
import os
import csv

# Set the path for the CSV file
election_csv = os.path.join("Resources", "election_data.csv")

# reading the CSV file
with open(election_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    header = next(csvreader)

    # set variable to store total no. of votes
    total_votes = 0
    candidate_vote_count = 0
    winner_vote_count = 0
    winner = ""

    # create list to store candidates
    candidates=[]
    unique_candidates = []
    vote_count = []
    vote_percent = []
    unique_candidates = []
    
    # variable to store column index for Candidates
    candcol = header.index("Candidate")
    
    # looping through the rows in csv reader
    for row in csvreader:

        #create counter variable
        total_votes +=1 

        # appending candidate names to list of candidates
        candidates.append(row[candcol])

    # creating a list for unique candidate names only
    unique_candidates = set(candidates)

    # alphabetically sorting candidates 
    unique_candidates = sorted(unique_candidates)

    # looping through  count of unique candidates
    for cand in unique_candidates:
        vote_count.append(0)
        vote_percent.append(0)

    # variable to represent index 
    x = 0

    # nested loop that will search unique candidate among the  candidates
    for cand in unique_candidates:
        for votes in candidates:
            if cand == votes:
                vote_count[x] += 1
        
        x=x+1
    
    # loop through all unique candidates 
    for y in range(len(unique_candidates)):
        vote_percent[y] = "{:.3%}".format(vote_count[y]/total_votes) 


# creating a dictionary for candidates and the votes they received 
dict = {"Candidates": unique_candidates, "Votes": vote_count, "Percentage" : vote_percent  }

# print output

print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("-------------------------")
print("")

# looping through the lists in the dictionary
for y in range(len(unique_candidates)):
    print(f"{dict['Candidates'][y]}: {dict['Percentage'][y]} ({dict['Votes'][y]})")
    print("")

print("-------------------------")
print("")

# finding the winner
print(f"Winner: {unique_candidates[vote_count.index(max(vote_count))]}") 
print("")        
print("-------------------------")

# creating the path for.txt file
filepath = os.path.join("analysis", "Election Results.txt")
f= open(filepath, "w")

# printing the .txt file

print("Election Results", file = f)
print("", file = f)
print("-------------------------", file = f)
print("", file = f)
print(f"Total Votes: {total_votes}", file = f)
print("", file = f)
print("-------------------------", file = f)
print("", file = f) 

# looping through the lists in the dictionary
for y in range(len(unique_candidates)):
    print(f"{dict['Candidates'][y]}: {dict['Percentage'][y]} ({dict['Votes'][y]})", file = f)
    print("", file = f)

print("-------------------------", file = f)
print("", file = f)

# finding the winner
print(f"Winner: {unique_candidates[vote_count.index(max(vote_count))]}", file = f)  
print("", file = f)       
print("-------------------------", file = f)

#closing the .txt file
f.close()
