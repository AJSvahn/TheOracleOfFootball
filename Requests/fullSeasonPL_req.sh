#!/bin/sh
#Call with the api key file

api=$(cat $1)

curl -X GET https://api.football-data.org/v2/competitions/PL/matches?SCHEDULED --header "X-Auth-Token:$api"  
