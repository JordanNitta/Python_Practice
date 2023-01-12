from flask import Flask, render_template, redirect, request

#this is going to import the users class in user.py
from user import User

app = Flask(__name__)

#when the page open it will route to /user/new
@app.route('/')
def index():
    return redirect('/users/new')

#Will render the template new_users and the page will be called /users/new
@app.route('/users/new')
def users():
    return render_template("new_users.html")

#This will process are form we submit and direct us to /users to show the users who got created
@app.route('/users/new', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/show/user/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    return render_template("user_display.html", user=User.get_one_user(data))

#this will just render are users_show page so when we submit the form this page will be rendered
@app.route('/users')
def list_of_users():
    return render_template('users_show.html', users=User.get_all())

@app.route('/users/<int:id>/edit')
def edit_page(id):
    data = {
        "id": id
    }
    return render_template("edit_users.html", user=User.get_one_user(data))

@app.route('/users/<int:id>/update', methods=['post'])
def update(id):
    data = {
        **request.form,
        'id': id
    }
    User.update(data)
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete_user(id):
    data = {
        'id': id
    }  
    User.delete_user(data)
    return redirect('/users')





if __name__ == "__main__":
    app.run(debug=True)