#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
import pandas
import json
import csv


# In[61]:


#Returns an integer code of the prediction, 0= home team, 2=away team, 1= draw.
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
        return 1
        
    
    if(homeXg > awayXg):
        return 0
    else:
        return 2


# In[1]:


#Takes the schedule, teamInfo parsed dictionaries (JSON) and the xG input (CSV). Runs through the schedule, pulling out team-ids and running the
#bestXgTeam function to return the higher wieghted xGteam. Returns a list of teamIDs and integer prediction code.

def doSimpleXgPredict(schedule, xG_in):
    
    predictions=[]
    matchday=int(schedule["filters"]["matchday"])
    for match in schedule['matches']:
        predictions.append( (match['homeTeam']['id'],
                             match['awayTeam']['id'],
                             bestXgTeam((match['homeTeam']['id'], 
                                         match['awayTeam']['id']), xG_in, matchday)
                            ))
    
    return predictions


# In[8]:


def main(args):
    
    with open (args[0], 'r') as f:
        matchday = json.load(f)
    
    xG_in = pandas.read_csv(args[1])
    
    day = args[2]
    
    writer = csv.writer(open ( day+'.predict', 'w'), delimiter=',', lineterminator='\n')
    writer.writerow(['homeTeam', 'awayTeam', 'predict'])
    for p in doSimpleXgPredict(matchday, xG_in): #iterates through list of teamIDs and returns team name from teamInfo
        writer.writerow(p)


# In[ ]:


#If run as a standalone script. Note the argv[1:] skips the first argument which is the script name

if __name__=="__main__":
    main(sys.argv[1:])
    


# In[ ]:




