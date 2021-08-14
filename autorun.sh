#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 dailymotion_m3ugrabber.py > ../dailymotion-US.m3u
python3 dailymotion_m3ugrabber.py "207.180.193.24:3128" > ../dailymotion-EU.m3u
python3 dailymotion_m3ugrabber.py "104.248.150.190:3128" > ../dailymotion-SG.m3u
echo m3u grabbed
