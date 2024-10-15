@echo off

echo Activating virtual environment...
call "%~dp0Battle-of-Warships\Scripts\activate"

echo Installing requirements...
cd "%~dp0\Battle-of-Warships"
python main.py

