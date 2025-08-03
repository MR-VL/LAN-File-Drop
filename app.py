import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, send_file
from werkzeug.utils import secure_filename
import netifaces as ni
import qrcode
import mimetypes
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

def get_local_ip():
    for iface in ni.interfaces():
        addresses = ni.ifaddresses(iface)
        if ni.AF_INET in addresses:
            for address in addresses[ni.AF_INET]:
                ip = address['addr']
                if ip and not ip.startswith('127.'):
                    return ip

    return '127.0.0.1'

# Main entry point to the app takes you to index page
@app.route('/')
def index():
    local_ip = get_local_ip()
    url = f"http://{local_ip}:5000"
    qr = qrcode.make(url)
    qr_path = os.path.join('static', 'qrcode.png')
    os.makedirs('static', exist_ok=True)
    qr.save(qr_path)
    return render_template('index.html', qr_path=qr_path, local_url=url)


# Upload route responsible for uploading files to server
@app.route('/upload', methods= ['POST'])
def upload_file():
    # If there are no files uploaded return a error message
    if 'files[]' not in request.files:
        return {'status': 'error', 'message': 'No file part'}, 400

    # Retrieves all the uploaded files from the frontend, is able to handle multiple files at once
    files = request.files.getlist('files[]')

    success_files = []
    failed_files = []

    # Loops through all the files uploaded
    for file in files:
        if file:
            # Sanitize the filename to avoid directory traversal attacks and unsafe characters
            filename = secure_filename(file.filename)

            if not allowed_file(filename):
                failed_files.append({'filename': filename, 'reason': 'File type not allowed'})
                continue

            try:
                # Save the file to the upload folder specified above
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                success_files.append(filename)

            except Exception as e:
                failed_files.append({'filename': filename, 'reason': str(e)})

    return {
        'status': 'ok',
        'uploaded': success_files,
        'failed': failed_files
    }

@app.route('/files')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = [f for f in files if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]
    return render_template('files.html', files=files)

@app.route('/download/<filename>')
def download_files(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return abort(404)

@app.route('/view/<filename>')
def view_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    return abort(404)

# Ensure app is being run locally and define params
# Host 0.0.0.0 allows the web server to be exposed to all devices on the local network
# Port is used to establish connection to web server

# WARNING: If port is occupied please specify a different one and try again
if __name__ == '__main__':
    # Print that the app has successfully started
    print("App started on port 5000")

    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug = True
    )
