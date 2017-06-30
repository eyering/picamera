from picamera import PiCamera
from time import sleep
import datetime

def capture():
	camera = PiCamera()

	camera.resolution = (2592,1944)
	#camera.frame=15

	camera.start_preview(alpha=200)
	a=datetime.datetime.now()
	a=a.strftime('%Y-%m-%d %H:%M:%S')
	camera.capture('/home/jbai/data/%s.jpg' % a)
	camera.stop_preview()

