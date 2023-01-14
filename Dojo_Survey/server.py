from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name'] # the request.form is the value and the session is the key
    session['dojo-location'] = request.form['dojo-location']
    session['favorite-language'] = request.form['favorite-language']
    session['comments'] = request.form['comments']
    print(session) #print out as dictionary
    return redirect('/show')
    #this will redirect to the show page

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

