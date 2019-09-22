#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[6]:


with open ('jsonOutput/6standings.json', 'r') as f:
    standings = json.load(f)


# In[44]:


with open ('jsonOutput/6schedule.json', 'r') as g:
    schedule = json.load(g)


# In[43]:


#Pay attention to the nesting of dictionary values.

#for team in standings['standings'][0]['table']:
#    print("%d: %s with ID:%d" % (team['position'], team['team']['name'], team['team']['id']))


# In[52]:


#for x in schedule['matches'][0]:
#    print("%s" % x)


# In[56]:


#for match in schedule['matches']:
#    print("%s vs. %s" % (match['homeTeam']['name'], match['awayTeam']['name']))


# In[138]:


#Returns the team higher in the ladder and the difference in places between the pair.

def bestestTeam (teamIDs):
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
        


# In[142]:


def doPredict():
    
    predictions=[]
    
    for match in schedule['matches']:
        predictions.append(
            bestestTeam((match['homeTeam']['id'], 
                         match['awayTeam']['id']))
                            )
            
    for p in predictions:
        print ("%s, %d point(s) seperate the teams" % (p[0], p[1]))
        
    



# In[143]:


doPredict()


# In[ ]:



    
    

