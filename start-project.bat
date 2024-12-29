@echo off

cd DjangoPy

:: Create the virtual environment
echo Creating virtual environment...
py -m venv .venv

:: Activate the virtual environment
echo Activating virtual environment...
.venv\Scripts\activate.bat

:: Install dependencies
echo Installing dependencies...
py -m pip install -U pip
pip install -r requirements.txt

:: Apply database migrations
echo Applying migrations...
python manage.py migrate

:: Run the Django server
echo Running Django server on port 8000...
python manage.py runserver

:: Deactivate virtual environment after server stops
echo Press Ctrl+C to stop the server.
pause
deactivate
