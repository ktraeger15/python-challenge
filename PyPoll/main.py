# CSV reader and os
import csv
import os
import collections

#Variables to count total votes cast and percentage votes
total_vote = 0
percentage_votes = 0

#Counts votes for each candidate
#Source: https://stackoverflow.com/questions/9247241/python-algorithm-of-counting-occurrence-of-specific-word-in-csv 
#Source: https://docs.python.org/3/library/collections.html 
candidate_votes_dict = collections.Counter()

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, "r") as csv_file: 
    csv_reader = csv.reader(csv_file)

    #Skip headers 
    next(csv_reader)

    for line in csv_reader: 
        #Creates a dictionary with candidate name as the key and total number of votes they received as the value 
        #Source: https://stackoverflow.com/questions/9247241/python-algorithm-of-counting-occurrence-of-specific-word-in-csv
        #Source: https://docs.python.org/3/library/collections.html 
        candidate_votes_dict[line[2]] += 1

for value in candidate_votes_dict.values():
    #Calculates the total votes from dictionary
    total_vote += value

#Opens a text file
txtpath = os.path.join("Analysis", "Election_Results.txt")
file = open(txtpath, "x")

#Outputs
print(f"Election Results")
file.write(f"Election Results \n")
print(f"Total Votes: {total_vote}")
file.write(f"Total Votes: {total_vote} \n")


#Source: https://realpython.com/iterate-through-dictionary-python/#iterating-through-dictionaries-comprehension-examples
for key, value in (candidate_votes_dict.items()):
    #Calculates the percentage of the vote each candidate receives and formats it
    percentage_votes = round((value/total_vote)*100,3)
    #Prints the candidate name, the percentage of votes they received, and the number of votes they received
    print(f"{key} {percentage_votes}% ({value})")
    file.write(f"{key} {percentage_votes}% ({value})\n")
    percentage_votes = 0

#Prints winner
#Source: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-80.php#:~:text=Use%20max()%20with%20the,value%20in%20the%20given%20dictionary.
print(f"Winner: {max(candidate_votes_dict, key=candidate_votes_dict.get)}")
file.write((f"Winner: {max(candidate_votes_dict, key=candidate_votes_dict.get)}"))
