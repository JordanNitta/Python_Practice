from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if "times_user_visit" not in session:
        session["times_user_visit"] = 1

    else:
        session["times_user_visit"] += 1

    return render_template("index.html")


@app.route('/add_to_visits')
def view_visits():
    if "times_user_visit" not in session:
        session["times_user_visit"] = 1

    else:
        session["times_user_visit"] += 1

    return redirect('/')


@app.route('/destroy')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)