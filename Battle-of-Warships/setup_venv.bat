@echo off

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call "%~dp0venv\Scripts\activate"

echo Installing requirements...
cd "%~dp0"
pip install -r "%~dp0\requirements.txt"

pause
