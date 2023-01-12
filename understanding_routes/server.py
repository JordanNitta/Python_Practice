from flask import Flask, render_template
app = Flask(__name__)

#Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def hello_world():
    return "Hello World"

#Create a route that responds with "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

#Create a route that responds with "Hi" and whatever 
# name is in the URL after /say/
@app.route('/hello/<name>')
def say_name(name):
    return f"Hi {name}"

#Create a route that responds with the given word 
# repeated as many times as specified in the URL
@app.route('/repeat/<int:num>/<string:word>') #The colon will cast it into the url
def repeat(num, word):
    output = ''
    for i in range(0,num):
        output += f"<h1>{word}</h1>"
    return output
    #return f"{word * num}"
    

        



if __name__=="__main__":
    app.run(debug=True, port=5001)