@echo off

echo Creating your playlist...
cd scripts
python dailymotion_m3ugrabber.py > ../dailymotion.m3u

pause
