#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import sys


# In[50]:


#Returns a single teamID of the higher ranked team in the GF rankings.
#Takes a pair of teamIDs and the lookup table of ID, ranking (teamInfo.json)

def bestGfTeam (teamIDs, teamInfo):
    homeRank=-1; awayRank=-1
    for team in teamInfo['teams']:
        if team['id'] == teamIDs[0]:
            homeRank = team['gf_position']
        elif team['id'] == teamIDs[1]:
            awayRank = team['gf_position']
    
    if(homeRank < 0 or awayRank < 0):
            return "Unable to grab points for one or both teams"
    
    
    if((homeRank - awayRank == 1) or (awayRank - homeRank == 1)
          and ((homeRank >= 13) and (awayRank >= 13))):
        return(0)
        
    
    if(homeRank < awayRank):
        return (teamIDs[0])
    else:
        return (teamIDs[1])


# In[14]:


#Takes the schedule and teamInfo parsed dictionaries. Runs through the schedule, pulling out team-ids and running the
#bestGfTeam function to return the higher team in the GF rankings. Returns a list of teamIDs from the iterated bestestTeam function.

def doTableBotPredict(schedule, teamInfo):
    
    predictions=[]
    
    for match in schedule['matches']:
        predictions.append(
            bestGfTeam((match['homeTeam']['id'], 
                         match['awayTeam']['id']), teamInfo)
                            )
    
    return predictions


# In[37]:


def lookupInfo(teamID, teamInfo):
    
    if (teamID == 0):
        return ("Draw")
    
    for team in teamInfo["teams"]:
        if team["id"] == teamID:
            return team["name"]
        
    return ("Could not match team ID to name")


# In[35]:


#Runs the prediction. The argument is a list of the schedule .json file and 
# the teamInfo with GF ranking .json file to be parsed in. Prints the
#resulting predictions in formatted strings.

def main(args):
    
    with open (args[0], 'r') as f:
        matchday = json.load(f)
    
    with open (args[1], 'r') as g:
        teamInfo = json.load(g)
    
    for p in doTableBotPredict(matchday, teamInfo):
        print ("%s" % lookupInfo(p, teamInfo))
    


# In[ ]:


#If run as a standalone script. Note the argv[1:] skips the first argument which is the script name

if __name__=="__main__":
    main(sys.argv[1:])
    
    

