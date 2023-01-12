from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def load_page():
    return "User http://127.0.0.1:5001/play or http://127.0.0.1:5001/play/10 or any number of boxes you want it to display"

@app.route('/play')
def play():
    return render_template("playground.html")


@app.route('/play/<boxes>')
def play_box(boxes):
    repeat_boxes = int(boxes)
    return render_template("playground1.html", repeat_boxes=repeat_boxes)

@app.route('/play/<boxes>/<color>')
def play_box_3(boxes, color):
    repeat_boxes = int(boxes)
    return render_template("playground2.html", repeat_boxes=repeat_boxes, color=color)

if __name__=="__main__":
    app.run(debug=True, port=5001)