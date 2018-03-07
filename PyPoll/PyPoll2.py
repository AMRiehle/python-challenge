candidates = []
votes_cast = {}
candidate_tally = {}

import os
csvpath = os.path.join('resources', 'election_data_2.csv')

import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        if row[0] != "Voter ID":
            votes_cast[row[0]] = row[2]
            if row[2] != "Candidate" and row[2] not in candidates:
                candidates.append(row[2])

from collections import defaultdict
counter = defaultdict(int)
                
for key, value in votes_cast.items():
    counter[value] += 1
        
for candidate in candidates:
    if candidate not in candidate_tally:
        candidate_tally[candidate] = counter[candidate]

print("Election Results:")
print("-----------------------")
print("Total Votes: " + str(len(votes_cast)))
print("-----------------------")

from decimal import Decimal

for key, value in candidate_tally.items():
    print(key + ": " + str(round(Decimal((value/len(votes_cast) * 100)), 1)) + "% (" + str(value) + ")")

print("-----------------------")

import operator    
max_key = max(candidate_tally.items(), key=operator.itemgetter(1))[0]

print("Winner: " + max_key)
print("-----------------------")

f = open('output/PyPoll2.txt','w')
f.write("Election Results:\n")
f.write("-----------------------\n")
f.write("Total Votes: " + str(len(votes_cast)) + "\n")
f.write("-----------------------\n")

for key, value in candidate_tally.items():
    f.write(key + ": " + str(round(Decimal((value/len(votes_cast) * 100)), 1)) + "% (" + str(value) + ")\n")

f.write("-----------------------\n")
f.write("Winner: " + max_key + "\n")
f.write("-----------------------\n")
f.close()