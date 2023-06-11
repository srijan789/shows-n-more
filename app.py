import os
from flask import Flask
from application.database import db
from application.config import LocalDevConfig
from flask_migrate import Migrate
app = None

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    '''
    Creates the app
    '''


    app = Flask(__name__, template_folder='templates')
    app.config.from_object(LocalDevConfig)
    db.init_app(app)

    migrate = Migrate(app, db)


    app.app_context().push()

    
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
