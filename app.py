import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory

# Declares the folder where files uploaded to the web server will be stored.
# You can manually change this by including the full 'C' drive path to your preferred location
UPLOAD_FOLDER = 'uploads'

# Lists the allowed extensions you may add more as necessary, the ones below are tested and are confirmed to work as
# intended, adding new extensions could potentially create problems during transfer
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'pdf', 'txt', 'zip', 'rar', 'mp3', 'tar', 'wav', 'm4a'}


# Creates a new Flask web application instance
app = Flask(__name__)

# Sets configuration in Flask app to store the uploaded files, this could change location (see above)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Checks to see if the desired folder exists already or not, if not it creates teh folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)