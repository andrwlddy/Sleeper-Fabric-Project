#!/usr/bin/env python
# coding: utf-8

# ## 24/25 initial data pull
# 
# New notebook

# In[11]:


# Import the requests library. Python uses this to send HTTP requests to the Sleeper API.
import requests

# Unique ID that tells Sleeper which league to retrieve data from
league_id = "1182197979838910464"

# Create one master list to store all matchup records
all_matchups = []

# Loop through each fantasy week (1-17)
for week in range(1, 18):

    # Build API URL for the current week
    url = f"https://api.sleeper.app/v1/league/{league_id}/matchups/{week}"
    
    # Send API request and convert response from JSON into Python objects
    response = requests.get(url)
    data = response.json()

    # Add season and week metadata before storing records (sleeper doesnt pull year data, only league ID is unique per year)
    for matchup in data:
        matchup["week"] = week
        matchup["season"] = 2025
        
        # Add matchup record to master dataset
        all_matchups.append(matchup)

# Preview first few records to validate API pull
print(all_matchups[:5])


# In[12]:


# Import JSON library to write Python objects into JSON files
import json


# Define the location in the Fabric Lakehouse where the raw matchup data will be stored
file_path = "/lakehouse/default/Files/matchups_2025.json"


# Save the API response data as a raw JSON file in the Lakehouse Files area
# This creates the Bronze layer source file that will be transformed into Delta tables later
with open(file_path, "w") as f:
    json.dump(all_matchups, f)


# Confirm successful file creation
print("Saved!")


# In[13]:


# Import operating system library to interact with file directories
import os


# Verify the Lakehouse directory structure and confirm saved files are available
print(os.listdir("/lakehouse/default"))

# Display files stored in the Lakehouse Files area
# Used to validate that the JSON file was successfully created
print(os.listdir("/lakehouse/default/Files"))


# In[14]:


# Import libraries used to retrieve API data and save JSON files
import requests
import json


# Unique ID for the 2024 Sleeper league
league_id = "1072575253525798912"


# Create empty list to store all matchup records from the 2024 season
matchups_2024 = []


# Loop through each fantasy week and retrieve matchup data from Sleeper API
for week in range(1, 18):

    # Build API endpoint for the current week
    url = f"https://api.sleeper.app/v1/league/{league_id}/matchups/{week}"
    
    # Pull matchup data and convert JSON response into Python objects
    response = requests.get(url)
    data = response.json()
    
    # Add season and week context before combining records
    # These fields are needed to differentiate seasons when data is combined
    for matchup in data:
        matchup["week"] = week
        matchup["season"] = 2024
        
        # Add matchup record to 2024 season dataset
        matchups_2024.append(matchup)


# Validate ingestion by displaying record count and sample records
print(f"Total records: {len(matchups_2024)}")
print(matchups_2024[:2])


# In[15]:


# Define the location where the raw 2024 matchup data will be stored in the Fabric Lakehouse
file_path = "/lakehouse/default/Files/matchups_2024.json"


# Save the 2024 matchup dataset as a raw JSON file in the Lakehouse Files area
# This preserves the original API response before any transformations are applied
with open(file_path, "w") as f:
    json.dump(matchups_2024, f)


# Confirm successful file creation
print("Saved!")


# In[16]:


# Import libraries used to retrieve API data and save JSON files
import requests
import json


# Store league IDs by season.
# Each season has a different Sleeper league ID.
leagues = {
    2024: "1072575253525798912",
    2025: "1182197979838910464"
}


# Loop through each season and retrieve related league data
for year, league_id in leagues.items():
    

    # -------------------------
    # Retrieve roster data
    # -------------------------
    
    # Build API endpoint to retrieve league rosters
    roster_url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    
    # Pull roster data from Sleeper API
    rosters = requests.get(roster_url).json()


    # Define Lakehouse storage location for raw roster data
    roster_file = f"/lakehouse/default/Files/rosters_{year}.json"


    # Save raw roster API response to Lakehouse Files area
    with open(roster_file, "w") as f:
        json.dump(rosters, f)

    print(f"Saved rosters_{year}.json")



    # -------------------------
    # Retrieve user/owner data
    # -------------------------

    # Build API endpoint to retrieve league users
    users_url = f"https://api.sleeper.app/v1/league/{league_id}/users"
    
    # Pull user data from Sleeper API
    users = requests.get(users_url).json()


    # Define Lakehouse storage location for raw user data
    users_file = f"/lakehouse/default/Files/users_{year}.json"


    # Save raw user API response to Lakehouse Files area
    with open(users_file, "w") as f:
        json.dump(users, f)

    print(f"Saved users_{year}.json")


# In[17]:


# Import libraries used to retrieve API data and save JSON files
import requests
import json


# Sleeper endpoint containing the master NFL player database
url = "https://api.sleeper.app/v1/players/nfl"


# Retrieve player reference data from Sleeper API
players = requests.get(url).json()


# Validate the API response by checking number of players returned
print(f"Total players: {len(players)}")


# Define location where raw player data will be stored in the Fabric Lakehouse
file_path = "/lakehouse/default/Files/players_nfl.json"


# Save raw player data as JSON in the Lakehouse Files area
# This file will later be transformed into the Dim_Player table
with open(file_path, "w") as f:
    json.dump(players, f)


# Confirm successful file creation
print("Saved players_nfl.json")


# In[18]:


# Import libraries used to retrieve API data and save JSON files
import requests
import json


# Store draft IDs by season.
# Each fantasy season has a unique Sleeper draft identifier.
drafts = {
    2024: "1072575255698350080",
    2025: "1182197979838910465"
}


# Loop through each season and retrieve draft selections
for year, draft_id in drafts.items():

    # Build API endpoint to retrieve draft picks
    url = f"https://api.sleeper.app/v1/draft/{draft_id}/picks"


    # Retrieve draft data from Sleeper API
    picks = requests.get(url).json()


    # Add season and draft identifiers for future analysis
    # These fields provide context when combining multiple seasons
    for pick in picks:
        pick["season"] = year
        pick["draft_id"] = draft_id


    # Define Lakehouse storage location for raw draft data
    file_path = f"/lakehouse/default/Files/draft_picks_{year}.json"


    # Save raw draft data as JSON in the Lakehouse Files area
    with open(file_path, "w") as f:
        json.dump(picks, f)


    # Confirm successful file creation
    print(f"Saved draft_picks_{year}.json")

