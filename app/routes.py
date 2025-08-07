import socket
from flask import render_template
from app import app

@app.route('/')
def index():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = 'Unavailable'
    
    return render_template('index.html', hostname=hostname, ip_address=ip_address)
