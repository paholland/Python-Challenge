import csv
import os

csv_path = os.path.join('Resources','election_data.csv')
pathout = os.path.join('Resources','election_results.txt')

total_votes = 0
winner_votes = 0
winner = ""
candidate_options = []
candidate_votes = {}

#read the data
with open(csv_path) as election_data:

    reader = csv.reader(election_data)
  

    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1 
        candidate_name  = row[2]

#      print(candidate_name)
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
            # print(candidate_name)
            # print(candidate_votes[candidate_name])
        candidate_votes[candidate_name]= candidate_votes[candidate_name] +1

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    if (votes > winner_votes):
        winner_votes = votes
        winner = candidate
    Percentage = float(votes)/float(total_votes)*100
 
#print 
print()
print('Election Results')
print('------------------------------')
print('Total Votes: ' + str(total_votes))
print('------------------------------')

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    Percentage = round(float(votes)/float(total_votes)*100,3)
    print(candidate + ' ' + str(Percentage) + '% ' + '('+ str(votes) + ')')

print('------------------------------')
print('Winner: '+str(winner))
print('------------------------------')

# outputing  files
with open(pathout, 'w') as txt_file:
    txt_file.write('Election Results')
    txt_file.write('\n')
    txt_file.write('------------------------------')
    txt_file.write('\n')
    txt_file.write
    txt_file.write(str(winner))
    txt_file.write('\n')
    txt_file.write('------------------------------')
    txt_file.write('\n')
    txt_file.write('Winner: ' + str(winner))
    txt_file.write('\n')
    txt_file.write('Total Votes' + str(votes)
    #txt_file.close()
    )