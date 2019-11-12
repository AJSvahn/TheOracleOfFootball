#!/bin/sh

for day in {1..11}
do
	python simpleXgBot_csvOutput.py ../jsonOutput/$day.matchday $1 $day
done
