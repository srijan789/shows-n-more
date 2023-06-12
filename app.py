import os
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api
from application.database import db
from application.config import LocalDevConfig
from application.models import *
from application.api import *



app = None
api = None


basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    '''
    Creates the app and api
    '''
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(LocalDevConfig)
    db.init_app(app)
    api = Api(app)
    migrate = Migrate(app, db)

    app.app_context().push()   
    return app, api

app, api = create_app()

api.add_resource(UserAPI, "/api/v1/user" "/api/v1/user/<int:id>")
api.add_resource(ShowAPI, "/api/v1/show" "/api/v1/show/<int:id>")
api.add_resource(VenueAPI, "/api/v1/venue" "/api/v1/venue/<int:id>")
api.add_resource(EventAPI, "/api/v1/event" "/api/v1/event/<int:id>")
api.add_resource(TagAPI, "/api/v1/tag" "/api/v1/tag/<int:id>")
api.add_resource(EventTagAPI, "/api/v1/eventtag" "/api/v1/eventtag/<int:id>")
api.add_resource(RatingAPI, "/api/v1/rating" "/api/v1/rating/<int:id>")
api.add_resource(BookingAPI, "/api/v1/booking" "/api/v1/booking/<int:id>")
api.add_resource(OrderAPI, "/api/v1/order" "/api/v1/order/<int:id>")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
