#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
import sys


# In[4]:


#Returns the team higher in the ladder and the difference in places between the pair.

def bestestTeam (teamIDs, standings):
    homeName="";   awayName=""; #Clunky, generate a team/ID lookup table to be imported into all bots.
    homePoints=-1; awayPoints=-1
    for team in standings['standings'][0]['table']:
        if team['team']['id'] == teamIDs[0]:
            homeName = team['team']['name']
            homePoints = team['points']
        elif team['team']['id'] == teamIDs[1]:
            awayName = team['team']['name']
            awayPoints = team['points']
    
    if(homePoints < 0 or awayPoints < 0):
            return "Unable to grab points for one or both teams"
    
    
    if(homePoints > awayPoints):
        return (homeName, homePoints - awayPoints)
    elif(homePoints < awayPoints):
        return (awayName, awayPoints - homePoints)
    else:
        return ("Draw", 0)
        


# In[2]:


#Takes the schedule and standing parsed dictionaries. Runs through the schedule, pulling out team-ids and running the
#bestestTeam function to return the higher team. Returns a list of pairs returned from the iterated bestestTeam function.
#i.e. (Winning team name, points seperating)

def doTableBotPredict(matchday, standings):
    
    predictions=[]
    
    for match in matchday['matches']:
        predictions.append(
            bestestTeam((match['homeTeam']['id'], 
                         match['awayTeam']['id']), standings)
                            )
    
    return predictions
        
    



# In[5]:


#Runs the prediction. The argument is a list of standings .json file and schedule .json file to be parsed in. Prints the
#resulting predictions in formatted strings.

def main(args):
    
    with open (args[0], 'r') as f:
        matchday = json.load(f)
    
    with open (args[1], 'r') as g:
        standings = json.load(g)
    
    for p in doTableBotPredict(matchday,standings):
        print ("%s, %d point(s) seperate the teams" % (p[0], p[1]))
    


# In[7]:


#If run as a standalone script. Note the argv[1:] skips the first argument which is the script name

if __name__=="__main__":
    main(sys.argv[1:])
    
    


# In[ ]:




