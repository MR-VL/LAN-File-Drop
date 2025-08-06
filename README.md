# LAN FileDrop

**LAN FileDrop** is a lightweight, zero-cloud Python web application that allows you to easily transfer photos, videos, and other files from your iPhone (or any device) to your laptop over your local network. No cables, no cloud syncs, and no third-party apps required.

Just open a browser on your phone, visit the local address provided by the app, and drag & drop as many files as you want. They'll be uploaded directly to your laptop.

---

## Features

- **Mobile-Friendly UI** — Designed to work seamlessly from iPhones and other mobile browsers.  
- **Unlimited Uploads** — No artificial limits on file sizes or number of files.  
- **LAN-Based** — Runs on your local network only. Nothing is sent to the cloud.  
- **Auto Save** — Files are instantly saved to a chosen directory on your laptop.  
- **Modern Design** — Clean, responsive HTML/CSS interface.

---

## Use Case

You’re on your iPhone and want to quickly send a bunch of videos or screenshots to your Linux/Windows laptop. Instead of emailing yourself or dealing with Apple’s closed ecosystem, just open this app on your laptop and visit the provided local IP on your iPhone to upload everything wirelessly.

---

## Tech Stack

- **Python 3.x**  
- **Flask** for the backend  
- **HTML5 / CSS3 / JavaScript** for the frontend  

---

## Installation

1. **Clone the repository**  
   `git clone https://github.com/yourusername/Lan-FileDrop.git`  
   `cd Lan-Filedrop`

   Please ensure that you have forked the repository to your account.

3. **Install dependencies**  
   `pip install -r requirements.txt`

4. **Run the app with Gunicorn**  
   `gunicorn -w 17 --threads 4 -b 0.0.0.0:5000 app:app`

   - `-w 17` — Run 17 worker processes (recommended: 2 × cores + 1)  
   - `--threads 4` — Each worker runs 4 threads (for better concurrency during uploads)  
   - `-b 0.0.0.0:5000` — Bind to all interfaces so the app is accessible from other LAN devices  
   - `app:app` — Target the Flask app instance named `app` inside `app.py`
   - Workers and threads can be set higher or lower depending on computer specs and memory availability
5. **Visit the app**  
   - On your **laptop**: `http://localhost:5000`  
   - On your **phone** (same Wi-Fi): `http://<your-laptop-local-ip>:5000`  
     e.g. `http://192.168.0.101:5000`

---

## Uploaded File Storage

Uploaded files are saved to the `uploads/` folder by default. You can change the directory path in `app.py` if needed.

---

<!-- ## Screenshot

![UI Screenshot](screenshot.png)

---
-->
## Future Features

- Add authentication or password protection for extra security 

---

## Contributions

Pull requests are welcome! If you have ideas for improvements like progress bars, password protection, or file previews, feel free to fork and submit.

---

## License

MIT License

---

## Tip

Add an alias to make it easy to run:  
`alias filedrop="gunicorn -w 17 --threads 4 -b 0.0.0.0:5000 /path/to/lan-filedrop/app:app"`

Now just type `filedrop` in your terminal to launch the app.

---


> ✨ Because transferring files without AirDrop shouldn’t feel like escaping North Korea with a USB stick.

