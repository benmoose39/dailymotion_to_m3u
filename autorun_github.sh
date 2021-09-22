#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)/scripts/
python3 dailymotion_m3ugrabber.py > ../dailymotion-US.m3u

echo m3u grabbed
