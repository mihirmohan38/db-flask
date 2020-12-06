from os import system 
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

    @app.route("/spark")
    def tfidf() : 
        try : 
            system("<command to run the files>")
            f = open("/home/hadoop/answer.txt", "r")
            ans = f.readline().strip("\n") 
            f.close()
            return json.loads(json.dumps({"correlation": ans }))
        except : 
            return json.loads(json.dumps({"correlation" : "Fail"}))

        return app 
        
if __name__ == '__init__':
    app = create_app()
    app.run()    