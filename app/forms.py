from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.csrf import CSRFProtect

class NewPropForm(FlaskForm):
    title = StringField('Property Title', validators = [InputRequired()])
    description = TextAreaField ('Description', validators=[InputRequired()])
    noOfRooms = StringField('No. of Rooms', validators=[InputRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators= [InputRequired()])
    proptype = SelectField('Property Type ', choices=[('House'), ('Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['png', 'jpg'], 'Images only! (png, jpg)')])