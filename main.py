import os
from flask import Flask
from application.database import db

app = None

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__, template_folder='templates')
    db.init_app(app)
    app.app_context().push()
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
