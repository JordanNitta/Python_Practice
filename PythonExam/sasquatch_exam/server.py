from flask_app import app
from flask_app.controllers import users, sasquatches


if __name__ == '__main__':
    app.run(debug=True)