import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

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


# Function to ensure that the current file that is being uploaded is within the allowed extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Main entry point to the app takes you to index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods= ['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return 'No file part', 400

    files = request.files.getlist('files[]')

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return 'Files uploaded successfully!'

# Ensure app is being run locally and define params
# Host 0.0.0.0 allows the web server to be exposed to all devices on the local network
# Port is used to establish connection to web server

# WARNING: If port is occupied please specify a different one and try again
if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug = True
    )

    print("App started on port 5000")