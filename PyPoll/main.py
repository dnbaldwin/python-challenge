import os
import csv
from pathlib import Path

# Get path and resolve data file location

# base_path = Path(__file__).parent
base_path = Path(__file__)

input_path = (base_path / "../Resources/election_data.csv").resolve()
output_path = (base_path / "../Analysis/analysis.txt").resolve()

# Set variables

totalVotes = 0
currentCandidate = ""
candidateVotes = 0
name = []
votes = 1
candidateList = []
votesList = []
percentageVotes = []


summary = []

# open the datafile and count total votes

with open(input_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')


# print the header, but exclude it from analysis

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        totalVotes += 1

        # identify each row by candidate name

        currentCandidate = row[2]

        # check if candidate has been seen before and is already in the list. If so add votes in corresponding
        # position in votes list
        # if not, add it
        if currentCandidate in candidateList:
            listPosition = candidateList.index(currentCandidate)
            votes = +1
            # print(listPosition)
            votesList[listPosition] = votesList[listPosition] + 1

        else:
            candidateList.append(currentCandidate)
            votesList.append(votes)
            votes = +1

# calculate the percentage votes received by each candidate

percentList = [(k/totalVotes)*100 for k in votesList[:]]
output = ["%.2f" % elem for elem in percentList]
print(output)

print(candidateList)
print(votesList)
print(totalVotes)
print(percentList)

# find the winner with most votes

maxVotes = max(votesList)
print("maxVotes: ", maxVotes)
maxVotesIndex = votesList.index(maxVotes)
print("maxVotesIndex: ", maxVotesIndex)
maxVotesCandidate = candidateList[maxVotesIndex]
print(maxVotesCandidate)

# Output the results to analysis.txt file

with open(output_path, 'w') as outfile:
    outfile.write("\n")
    outfile.write("Election Results\n")
    outfile.write("\n")
    outfile.write("---------------------------\n")
    outfile.write("\n")
    outfile.write(f"Total Votes:  {totalVotes}\n")
    outfile.write("\n")
    outfile.write("---------------------------\n")
    outfile.write("\n")
    for i in range(len(candidateList)):
        summary = candidateList[i] + ":   " + \
            str(output[i] + "%  (" + str(votesList[i]) + ")")

        outfile.write(f"{summary} \n")

    outfile.write("\n")
    outfile.write("---------------------------\n")
    outfile.write("\n")
    outfile.write(f"Winner: {maxVotesCandidate}\n")
    outfile.write("\n")
    outfile.write("---------------------------\n")
