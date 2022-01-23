# HIGH LEVEL LIST:
# 1. The data we need to retrieve
# 2. The total number of votes cast 
# 3. A complete list of andidates who received votes
# 4. The total number of votes eash candidate won
# 5. The winner of the election based on popular vote.

#Import the datetime class from the datetime module.
import os
import csv
import datetime as dt
# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
# Print the present time.
print("The time right now is", now)
# Add our dependencies.
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
    #print(row)

    # Print the header row.
    #headers = next(file_reader)
    #print(headers)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


