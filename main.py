import subprocess
import serial
import cv2
from flask import Flask, Response, redirect, render_template

app = Flask(__name__)

def stream(camera_index):
    cam = cv2.VideoCapture(camera_index)
    while True:
        _, frame = cam.read()
        ret, jpg = cv2.imencode('.jpg', frame)
        jpg2bytes = jpg.tobytes()
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpg2bytes + b'\r\n\r\n'

@app.route('/')
def index():
	# Get Temperature
	temp = subprocess.run(['/usr/bin/vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	data = {
		'title': 'Index',
		'temp': temp.stdout
	}
	return render_template('index.html', **data)

@app.route('/stream')
def stream_feed():
    return Response(stream(0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/serial')
def get_serial():
	return Response('')

app.run(host='0.0.0.0', port=8000, debug=True)


