# InfoSys1D-backend
first git project to understand basics

The file first of all only runs if its on a conda env for some reason so you will need s a conda env. 

python files : 
simplejson 
waitress 


To work with the app you will need the following commands:

For Linux and Mac:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
For Windows cmd, use set instead of export:

set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
For Windows PowerShell, use $env: instead of export:

$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"
flask run


waitress-serve --port=8041 --call "flaskr:create_app"
waitress-serve --call "flaskr:create_app"    to run the app
waitress-serve --call "main:create_app"

Serving on http://0.0.0.0:8080
