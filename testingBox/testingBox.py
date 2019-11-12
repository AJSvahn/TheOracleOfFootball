#!/usr/bin/env python
# coding: utf-8

# In[48]:


import json
import pandas
import sys


# In[ ]:


#with open ("../jsonOutput/2.matchday", 'r') as f:
    #matchday = json.load(f)

#predictions = pandas.read_csv('gw2_100.csv')

#for x in range(0, len(pandaFrame)-1):
 #   print("%d: %s: %s" % (pandaFrame["ID"][x], pandaFrame["Total xG"][x]))


# In[ ]:


#Takes a matchday file requested after the day, with results. Fetches the winner and home and away ids. Converts the
#result text into integer code. 0 = home win, 1 = draw, 2 = away win. Returns an array of triples- (homeId, awayId, result). 

#def getMatchdayResults(matchday):

#    results=[]

#    for match in matchday["matches"]:
#        winner = match["score"]["winner"]
        #score_home = match["score"]["fullTime"]["homeTeam"] #Not required yet, may be useful when using to run tip scoring
        #score_away = match["score"]["fullTime"]["awayTeam"]
#        home_id = int(match["homeTeam"]["id"])
#        away_id = int(match["awayTeam"]["id"])
#        if(winner=="HOME_TEAM"):
#            results.append((home_id, away_id, 0))
#        elif(winner=="AWAY_TEAM"):
#            results.append((home_id, away_id, 2))
#        else:
#            results.append((home_id, away_id, 1))
                       
#    return results


# In[ ]:


#Takes an array of predictions and a matchday file requested after the day, with results. Fetches the winner and home and away ids that match the
#current prediction. The prediction use the integer code 0 = home win, 1 = draw, 2 = away win. 
#Returns an array of 1's and 0's indicating a correct or incorrect prediction for each match.

def matchdayCompare(predictionArray, matchday):

    results=[]
    
    for predict in predictionArray:                #iterates through predictions
        for match in matchday["matches"]:          #iterates through matches
            if (match["homeTeam"]["id"] == predict[0]):
                winner = match["score"]["winner"]
                #score_home = match["score"]["fullTime"]["homeTeam"] #Not required yet, may be useful when using to run tip scoring
                #score_away = match["score"]["fullTime"]["awayTeam"]
                if(winner=="HOME_TEAM" and predict[2]==0):
                    results.append(1)
                elif(winner=="AWAY_TEAM" and predict[2]==2):
                    results.append(1)
                elif(winner=="DRAW" and predict[2]==1):
                    results.append(1)
                else:
                    results.append(0)
                       
    return results


# In[ ]:


#for x in matchdayCompare(convertPredictionsToArray(predictions), matchday):
    #print (x)


# In[53]:


def convertPredictionsToArray (predictionsCSV):

    predict_array=[]

    for x in range(0, len(predictionsCSV)):
        predict_array.append( (predictionsCSV["homeTeam"][x], predictionsCSV["awayTeam"][x], predictionsCSV["predict"][x]))

    return predict_array


# In[ ]:


#for x in convertPredictionsToArray(predictions):
#    print (x)


# In[56]:


def lookupInfo(teamID, teamInfo):
    
    if (teamID == 0):
        return ("Draw")
    
    for team in teamInfo["teams"]:
        if team["id"] == teamID:
            return team["name"]
        
    return ("Could not match team ID to name")


# In[72]:


def main(args):
    
    with open (args[0], 'r') as f:
        matchday = json.load(f)
    
    picks = pandas.read_csv(args[1])
    
    print("%i" % sum(matchdayCompare(convertPredictionsToArray(picks), matchday)))       


# In[63]:


#If run as a standalone script. Note the argv[1:] skips the first argument which is the script name

if __name__=="__main__":
    main(sys.argv[1:])


# In[ ]:




