from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def create_ninja():
    return render_template('create_ninja.html', all_dojos = Dojo.get_all())
    

@app.route('/ninjas/create', methods=['POST'])
def ninja_create():
    Ninja.save_ninja(request.form)
    print(request.form)
    return redirect('/dojos')