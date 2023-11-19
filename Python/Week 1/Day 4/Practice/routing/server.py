from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  
@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojing():
    return 'Dojo!'

@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def hi(name):
    return "Hi {name}"

@app.route('/say/<int:id>/<name>')          # The "@" decorator associates this route with the function immediately following
def repeat(id,name):
    return f"{name} " * id



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 