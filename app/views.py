"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.forms import NewPropForm
from werkzeug.utils import secure_filename
from app.models import Property


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST', 'GET'])
def newProp():
    """Render the website's new property."""
    form = NewPropForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            noOfRooms = form.noOfRooms.data
            bathrooms = form.bathrooms.data
            price = form.price.data
            proptype = form.proptype.data
            location = form.location.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            newProperty = Property(title, description, noOfRooms, bathrooms, price, proptype, location, filename)
            db.session.add(newProperty)
            db.session.commit()
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('Property successfully added', 'success')
            return redirect(url_for('properties'))
    return render_template('newProperty.html', form=form)

@app.route('/properties/')
def properties():
    """Render the websites view properties page"""
    prop = Property.query.all()
    return render_template('properties.html', prop=prop)

@app.route('/properties/<propId>')
def viewProperty(propId):
    """Render the websites view property pages."""
    prop = Property.query.filter_by(id=propId).first()
    return render_template('viewProperty.html', prop=prop)


@app.route("/uploads/<filename>")
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
