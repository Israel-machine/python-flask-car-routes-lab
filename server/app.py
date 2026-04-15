#REQUIRED TO INIT FLASK
from flask import Flask #importing flask class from flask dependency in pipfil

app = Flask(__name__) #initializes app with flask class and passing name of application

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

#DEFAULT ROOT INIT
@app.route('/')#DECORATOR 
def index():
    return 'Welcome to Flatiron Cars'#returns HTML using ' '

#ROUTE MODEL
@app.route('/<string:model>')#dynamic route with <datatype: name of variable>
def user(model):#takes argument of string, named username
    if model in existing_models:#check if model is in "existing_model"
        return f'Flatiron {model} is in our fleet!'
    else:
        return f'No models called {model} exists in our catalog'

#run file directly on app.py using python app.py
if __name__ == '__main__':
    app.run(port=5555, debug=True)
