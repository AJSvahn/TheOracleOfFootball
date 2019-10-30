#!/bin/sh

for day in {9..10}
do
	printf "\n\nMatchday $day picks: \n\n"
	python simpleXgBot.py ../jsonOutput/$day.matchday teamInfo.link $1
done
