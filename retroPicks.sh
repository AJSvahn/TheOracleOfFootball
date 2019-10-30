#!/bin/sh

for day in {1..$1}
do
	printf "\n\nMatchday $day picks: \n\n"
	python simpleXgBot ../jsonOutput/$day.matchday $2 $3
done
