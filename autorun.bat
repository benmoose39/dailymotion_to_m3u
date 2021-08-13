@echo off

echo Creating your playlist...
cd scripts
python dailymotion_localrun.py > ../dailymotion.m3u

pause
