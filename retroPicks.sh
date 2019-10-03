#!/bin/sh

for day in {1..8}
do
	printf "\n\nMatchday $day picks: \n\n"
	python gfBot.py ../jsonOutput/$day.matchday teamInfo.link
done
