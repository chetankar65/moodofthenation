import json
import os
import sqlite3

# Third-party libraries
from flask import Flask, redirect, request, url_for, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

# Internal imports
from db import init_db_command
from user import User

# Configuration
### Set environment variables for GOOGLE_CLIENT_ID,GOOGLE_CLIENT_SECRET,GOOGLE_DISCOVERY_URL

#. ~/.bashrc - Run before starting server

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

# Flask app setup
app = Flask(__name__)
#app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)
app.secret_key = 'chetD0ne'

# User session management setup
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.unauthorized_handler
def unauthorized():
    return "You must be logged in to access this content.", 403

# Naive database setup
try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

## Retrieving google configuration information
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

################
@app.route("/")
def index():
    if current_user.is_authenticated:
        user = current_user.name
        return render_template('dashboard.html', user = user)
        #current_user.name, current_user.email, current_user.profile_pic
    else:
        return render_template('index.html')


### Login endppoint
@app.route('/login')
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to contruct request for google
    # scopes to retrieve user profile info

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri = request.base_url + "/callback",
        scope = ["openid", "email", "profile"],
    )

    return redirect(request_uri)


###Now make the dashboard
@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    # Now that we have tokens let's find and hit the URL
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400
        # Create a user in your db with the information provided
    # by Google
    user = User(
        id_=unique_id, name=users_name, email=users_email, profile_pic=picture
    )

    # Doesn't exist? Add it to the database.
    if not User.get(unique_id):
        User.create(unique_id, users_name, users_email, picture)

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))

### Logout the user if logged in
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
'''
@app.route('/news')
def news():
    top_headlines = newsapi.get_top_headlines(q='bitcoin',category='business',language='en',country='us')

    sources = newsapi.get_sources()

    print(top_headlines["articles"])
    for article in top_headlines["articles"]:
        print(article[0]["author"],article[0]["title"],article[0]["description"])
    return "Hi"
'''


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
    # This is done as a lot of google APIs do not work unless there is an SSL certificate.
    # The pythonSSL module creates an SSL certificate on the fly. There will be a warning
    # as the certificate is not verified, but we can advance.It's fine

#news api: cf454be3d2784854a6d0c0e3b6363c29