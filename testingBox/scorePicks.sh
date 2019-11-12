#!/bin/sh

for day in {1..11}
do

	python testingBox.py ../jsonOutput/$day.matchday shotsTest/$day.predict
done
