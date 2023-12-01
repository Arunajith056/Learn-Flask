#1
# Python Flask web development to import the Flask class from the flask module.
# The Flask class is a fundamental part of building web applications using Flask.
from flask import Flask 
#2
#we are creating a new instance of the Flask class and assigning it to a variable named app.
#This instance will be our web application object, 
#which we can use to handle incoming requests and responses.
app = Flask(__name__)
#3
#@app.route() decorator to create a route for the root URL of the web application.
@app.route('/')#The forward slash / represents the root URL.
def home():#This function will be executed when someone visits the root URL of the web application.
    return "Hello, world!" 
#4
#This statement ensures that the code block inside it only runs when the script is being ,
#executed directly and not when it's imported as a module.
if __name__ == '__main__':
    app.run(debug=True)#starts the Flask application with debug mode enabled.

    '''Debug mode provides additional information about errors and exceptions,
     making it easier to debug your application during development.
    ''' 