import os 
from flask import Flask 
import click
import json

def create_app(test_config = None) : 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = "dev", 
        )

    if test_config is None : 
        app.config.from_pyfile("config.py", silent = True )
    else : 
        app.config.from_mapping(test_config)

    @app.route("/hello")
    def hello(): 
        return "hello"

    @app.route("/tfidf/<mongo>")
    def tfidf(mongo) : 
        #run the tfidf file. 

        return "success json"

    @app.route("/pearson/<mongo>")
    def pearson(mongo) : 
        # run pearson file
        return mongo

    return app 
if __name__ == '__init__':
    app = create_app()
    app.run()    
