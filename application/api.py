from flask_restful import Resource
from flask_restful import fields, marshal_with
from .database import db
from .models import *


class UserAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class ShowAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class VenueAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class EventAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class TagAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class EventTagAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class RatingAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class BookingAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass

class OrderAPI(Resource):
    def get(self, id):
        pass
    def post(self):
        pass
    def delete(self, id):
        pass
    def put(self, id):
        pass