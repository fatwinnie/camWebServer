from picamera import PiCamera
from time import sleep

class smile(object):
	def Cap():
		camera = PiCamera()
		camera.hflip=True
		camera.vflip=True			
		sleep(5)	
		filename='/static/image/testme.jpg'		
		camera.capture('/home/pi/camWebServer2/static/image/testme.jpg')
		camera.close()
		return 'http://192.168.1.247:5000'+ filename
			
			
			
	
	


