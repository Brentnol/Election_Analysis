# HIGH LEVEL LIST:
# 1. The data we need to retrieve
# 2. The total number of votes cast 
# 3. A complete list of andidates who received votes
# 4. The total number of votes eash candidate won
# 5. The winner of the election based on popular vote.

#Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
# Print the present time.
print("The time right now is", now)
import csv
import os

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
    #print(election_data)
# Close the file.
# election_data.close()

# Create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file. 
#file_to_save = os.path.join("analysis","election_analysis.txt")
# Use the open statement to open the file as a text file.
#with open(file_to_save,"w") as txt_file:
# Write some data to the file.
    #txt_file.write("Hello World, ")
# Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
# Write three counties to the file.
    #txt_file.write("Arapahoe, Denver, Jefferson")
    #txt_file.write("Counties in the Election\n------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies.
# Assign a variable to load a file from a path.
#file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# To do: read and analyze the data here.
# Read the file object with the reader function.
