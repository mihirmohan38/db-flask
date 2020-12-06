
# Downloading and running 

git clone https://github.com/mihirmohan38/db-flask.git on set up.


cd db-flask/


waitress-serve --port=8041 --call "flaskr:create_app"




# BB - Flask server for anlytics tasks.

## CLI - Command 
waitress-serve --port=8041 --call "flaskr:create_app"


*sets up the server* 


Serving on http://0.0.0.0:8041


Note : Don't forget to open 8041 port in security group of the instance.


## End point 
http://ip-addr:8041/spark/


-> runs the pearson correlation and tfidf tasks.



## Dependencies 
waitress -> apt install python3-waitress

flask -> apt install python3-flask 

flask_cors -> pip3 install flask-cors


# BB - Flask server for anlytics tasks.

## Spark Job

##*tfidf*## data will be stored in hdfs file format in the location hdfs://localhost:9000/user/hadoop/output/

##*Pearson correlation*## will be stored in /home/hadoop/corr.txt and will be sent back as json string response.


