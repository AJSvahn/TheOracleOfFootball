#!/bin/sh

#To be called with an argument indicating the matchday and the api key

api=$(cat $2)
curl -X GET https://api.football-data.org/v2/competitions/PL/matches?matchday=$1 --header "X-Auth-Token:$api"  
