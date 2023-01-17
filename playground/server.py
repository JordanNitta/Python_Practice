from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def load_page():
    return render_template("home.html")

@app.route('/play')
def play():
    return render_template("playground.html")


@app.route('/play/<int:boxes>')
def play_box(boxes):
    return render_template("playground1.html", repeat_boxes=boxes)

@app.route('/play/<int:boxes>/<string:color>')
def play_box_3(boxes, color):
    return render_template("playground2.html", repeat_boxes=boxes, color=color)

if __name__=="__main__":
    app.run(debug=True, port=5001)