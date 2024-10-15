@echo off

echo Creating virtual environment...
python -m venv Battle-of-Warships

echo Activating virtual environment...
call "%~dp0Battle-of-Warships\Scripts\activate"

echo Installing requirements...
cd "%~dp0\Battle-of-Warships"
pip install -r requirements.txt

pause
