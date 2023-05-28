from flask_app import app, render_template, request, redirect, session
from flask_app.models.dojo import Dojo
# from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo_display():
    return render_template("create_dojo.html", all_dojos = Dojo.get_all())

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    Dojo.save_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def display_dojo_and_ninja(id):
    data = {
        'id': id
    }
    dojo = Dojo.get_all_dojo_ninja(data)
    return render_template('show.html', dojo = dojo)