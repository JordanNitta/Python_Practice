from flask_app import app, render_template, request, redirect, session, flash
from flask_app.models.sasquatch import Sasquatch
from flask_app.models.user import User



@app.route('/dashboard')
def recipes():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template("all_sasquatches.html", all_sasquatches=Sasquatch.get_all())

@app.route('/new/sighting')
def create_animal():
    return render_template('new_sighting.html')

@app.route('/process/sighting', methods=['POST'])
def process_animal():
    if not Sasquatch.validate_sasquatch(request.form):
        return redirect('/new/sighting')
    Sasquatch.save_sasquatch(request.form)
    print(request.form)
    return redirect('/dashboard')

# Renders page with an edit option and gets 
@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/login')
    data = {
        'id': id
    }
    return render_template('edit_animal.html', sasquatch = Sasquatch.get_one(data))

# Update recipe from form
@app.route('/update', methods=['POST'])
def process_update():
    if not Sasquatch.validate_sasquatch(request.form):
        return redirect(f'/edit/{request.form[id]}')
    Sasquatch.update(request.form)
    print(request.form)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def display_one(id):
    data = {
        'id': id
    }
    return render_template('show.html', sasquatch = Sasquatch.get_one(data))

@app.route('/delete/<int:id>')
def delete_recipe(id):
    data = {
        'id': id
    }
    Sasquatch.delete(data)
    return redirect('/dashboard')