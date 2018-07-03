#!/bin/bash
cd /home/MeanBot001/ComplimentBot
for ((i=0; i<=5; i++)); do
	echo 'New Loop Begun.'
        python3.6 ScheduledRun.py
    done
