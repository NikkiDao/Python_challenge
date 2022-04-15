import csv
import os

#creating filepath
election_data_csv = os.path.join('election_data.csv')

total_votes = 0 
votes_per_candidate = {}

with open(election_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skipping header row
    csv_header = next(csvreader)
    
# Read each row of data after the header
    for row in csvreader:
        total_votes += 1
        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1   
        
      

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votes_per_candidate, key=votes_per_candidate.get)

print(f"Winner: {winner}")

# output text file

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(totalVotes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in votes_per_candidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
 
