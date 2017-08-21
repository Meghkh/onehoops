from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

app.secret_key = "ABC"


# ROUTES GO HERE
@app.route('/')
def start_here():
    """Home page."""

    return render_template('index.html')


@app.route('/register')
def show_registration_detail_page():
    """Registration page."""

    return render_template('registration.html')


@app.route('/volunteer')
def show_volunteer_page():
    """Volunteer page."""

    pass


@app.route('/donate')
def show_donation_page():
    """Donation page."""

    pass


@app.route('/mission')
def show_mission_page():
    """Mission page."""

    pass


@app.route('/gallery')
def show_gallery_page():
    """Gallery page."""

    pass


@app.route('/contact')
def show_contact_page():
    """Contact page."""

    pass


if __name__ == '__main__':
    app.debug = True
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0", debug=True)
