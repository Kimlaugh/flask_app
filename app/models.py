import unicodedata
from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(250))
    rooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    price = db.Column(db.String(80))
    proptype = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(255))

    def __init__(self, title, description, rooms, bathrooms, price, proptype, location, photo):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.proptype = proptype
        self.location = location
        self.photo = photo


    def get_id(self):
        try:
            return unicodedata(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)