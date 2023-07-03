# Import modules os and csv
import os
import csv

# Set the path for the CSV file
election_csv = os.path.join("Resources","election_data.csv")

# Open the CSV using the set path PyPollcsv
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Set veriable to store data.
    total_votes = 0

    # Create list to store data
    candidates = []
    unique_candidates = []
    vote_count = []
    vote_percent = []

    # variable to store column index for Candidates
    candcol = header.index("Candidates")

    # Looping through the rows in csvreader
    for row in csvreader:

        # Use counter veriable to count the total votes
        total_votes +=1

        # appending candidate names
        candidates.append(row[candcol])

     # creating a list with unique candidate names only
    unique_candidates = set(candidates)

    # sort candidate names alphabetically
    unique_candidates = sorted(unique_candidates)

    # looping through number of unique candidates
    for candidates in unique_candidates:

    # appending values to vote count and percent lists
        vote_count.append(0)
        vote_percent.append(0)

    # variable to represent index
    x = 0

    # nested loop to look for each unique candidate from the candidates
    for candidates in unique_candidates:
        for votes in candidates:
            if candidates == votes:
                vote_count[x] += 1
        x=x+1

    # loop that goes through all unique candidates and assigns percentage values in the vote_percent[] list
    for y in range(len(unique_candidates)):
        vote_percent[y] = "{:.3%}".format(total_votes[y]/total_votes)


# creating a dictionary for candidates and there received votes and percentage votes
dict = {"Candidates": unique_candidates, "Votes": total_votes, "Percentage" : vote_percent  }

# print output

print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("-------------------------")
print("")

# looping through all the lists in the dictionary
for y in range(len(unique_candidates)):
    print(f"{dict['Candidates'][y]}: {dict['Percentage'][y]} ({dict['Votes'][y]})")
    print("")

# finding the winnig candidate
print(f"Winner: {unique_candidates[total_votes.index(max(total_votes))]}") 
print("")        
print("-------------------------")

# creating a .txt file

# setting the path for where the .txt file is saved
filepath = os.path.join("analysis", "PyPoll.txt")
f= open(filepath, "w")

# printing the output for .txt file

print("Election Results", file = f)
print("", file = f)
print("-------------------------", file = f)
print("", file = f)
print(f"Total Votes: {total_votes}", file = f)
print("", file = f)
print("-------------------------", file = f)
print("", file = f) 

# looping through all the lists in the dictionary
for y in range(len(unique_candidates)):
    print(f"{dict['Candidates'][y]}: {dict['Percentage'][y]} ({dict['Votes'][y]})", file = f)
    print("", file = f)

print("-------------------------", file = f)
print("", file = f)

# finding the winner
print(f"Winner: {unique_candidates[total_votes.index(max(total_votes))]}", file = f)  
print("", file = f)       
print("-------------------------", file = f)

#closing the .txt file
f.close()