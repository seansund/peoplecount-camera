import picamera

with picamera.PiCamera() as camera:
	filepath = "/var/image"
	filename = "image_1_test.jpg"
	
	camera.capture(filepath + filename)
