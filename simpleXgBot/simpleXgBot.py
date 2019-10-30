#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import pandas
import json


# In[62]:


#some code for testing
#with open ("2.matchday", 'r') as f:
        #matchday = json.load(f)
    
#with open ("teamInfo.link", 'r') as g:
        #teamInfo = json.load(g)
       
#xG_in = pandas.read_csv("xG_input_gw8.csv")

#bestXgTeam((397, 354), xG_in, 2)


# In[ ]:





# In[48]:





# In[61]:


#Returns a single teamID of the higher ranked team in the GF rankings.
#Takes a pair of teamIDs and the lookup table of ID, ranking (teamInfo.json)

def bestXgTeam (teamIDs, xG_in, matchday):
    homeXg=-1; awayXg=-1
    totalMatches=38
    for x in range(0, len(xG_in)):
        if xG_in['id'][x] == teamIDs[0]:
            homeXg = ( ( (1 - (matchday / totalMatches) ) * xG_in['past_xG'][x]) +
                        (matchday / totalMatches) * xG_in['current_xG'][x])
        elif xG_in['id'][x] == teamIDs[1]:
            awayXg = (((1 - (matchday / totalMatches)) * xG_in['past_xG'][x]) +
                        (matchday / totalMatches) * xG_in['current_xG'][x])
    
    if(homeXg < 0 or awayXg < 0):
            return "Unable to grab xG for one or both teams"
    
    
    if(abs(homeXg-awayXg) <= 0.005 ):
        return(0)
        
    
    if(homeXg > awayXg):
        return (teamIDs[0])
    else:
        return (teamIDs[1])


# In[6]:


#Takes the schedule, teamInfo parsed dictionaries (JSON) and the xG input (CSV). Runs through the schedule, pulling out team-ids and running the
#bestXgTeam function to return the higher wieghted xGteam. Returns a list of teamIDs.

def doSimpleXgPredict(schedule, xG_in):
    
    predictions=[]
    matchday=int(schedule["filters"]["matchday"])
    for match in schedule['matches']:
        predictions.append(
            bestXgTeam((match['homeTeam']['id'], 
                         match['awayTeam']['id']), xG_in, matchday)
                            )
    
    return predictions


# In[4]:


def lookupInfo(teamID, teamInfo):
    
    if (teamID == 0):
        return ("Draw")
    
    for team in teamInfo["teams"]:
        if team["id"] == teamID:
            return team["name"]
        
    return ("Could not match team ID to name")


# In[7]:


def main(args):
    
    with open (args[0], 'r') as f:
        matchday = json.load(f)
    
    with open (args[1], 'r') as g:
        teamInfo = json.load(g)
        
    xG_in = pandas.read_csv(args[2])
    
    
    for p in doSimpleXgPredict(matchday, xG_in):
        print ("%s" % lookupInfo(p, teamInfo))


# In[ ]:


#If run as a standalone script. Note the argv[1:] skips the first argument which is the script name

if __name__=="__main__":
    main(sys.argv[1:])
    

