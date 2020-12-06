# BB - Flask server for anlytics tasks.

## Dependencies 
waitress -> apt install python3-waitress
flask -> apt install python3-flask 
flask_cors -> pip3 install flask-cors

## CLI - Command 
waitress-serve --port=8041 --call "flaskr:create_app"
*sets up the server* 


Serving on http://0.0.0.0:8041
Note : Don't forget to open 8041 port in security group of the instance.


End point : ip:8041/spark/
-> runs the pearson correlation and tfidf tasks.


