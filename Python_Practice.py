from ensurepip import version
from platform import python_branch

counties = ["Arapahoe","Denver","Jefferson"]
counties_dict={}

#if "Arapahoe" in counties and "El Paso" is not counties:
    
    #print("Only Arapahoe is the list of counties.")
#else:
    #print("Arapahoe is in the list of counties and El Paso is not in list")

for county in counties:
    print(county)


numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

#counties_dict=[{"county":"Arapahoe", "registered_voters":422829},{"county":"Denver", "registered_voters":463353,},{"county":"Jefferson","registered_voters":432438}]

#for countiest_dict in registered_voters:

    
for county in counties_dict:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
for registered_voters in counties_dict:
    print(registered_voters)

for county in counties_dict.keys():
    print(county)

for registered_voters in counties_dict.values():
    print(registered_voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county,voters)

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},{"county": "Denver", "registered_voters": 463353},{"county": "Jefferson", "registered_voters": 432438}]

for i in range(len(voting_data)):
    print(voting_data[i]['registered_voters'])


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")


#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")



