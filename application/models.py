from .database import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String, nullable = True)
    duration = db.Column(db.Interval, nullable = False)
    rating = db.Column(db.Float, nullable = True)

class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    location = db.Column(db.String, nullable = False)
    capacity = db.Column(db.Integer, nullable = False)

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"), nullable = False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable = False)
    datetime = db.Column(db.DateTime, nullable = False)
    seats_available = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Float, nullable = False)

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String, nullable = False)

class EventTag(db.Model):
    __tablename__ = 'enventtag'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable = False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable = False)

class Rating(db.Model):
    __tablename__ = 'rating'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String, nullable = True)

class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    datetime = db.Column(db.DateTime, nullable = False)
    total_price = db.Column(db.Float, nullable = False)
    rating = db.Column(db.Integer, nullable = True)


