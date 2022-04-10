import csv
import os


totalVotes = 0 
votesPerCandidate = {}

#creating filepath
election_data_csv = os.path.join('C:\\Users\\Danny Dao\\Desktop\\UCI program\\HOMEWORK\\Python\\pypoll.py\\Resources\\election_data.csv')

with open(election_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skipping header row
    csv_header = next(csvreader)
    
# Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1   
        
      

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votesPerCandidate, key=votesPerCandidate.get)

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

for candidate, votes in votesPerCandidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')
 