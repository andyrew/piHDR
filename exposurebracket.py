import picamera
from time import sleep
from fractions import Fraction

# This script captures exposures with varying shutter time. 
# The frame rate needs to be longer than the exposure or it won't work. 
# The capture takes as long as the frame rate, so reducing the frame rate saves time for quick exposures.

with picamera.PiCamera() as camera:
    # detect camera version so that it resolution can be set
    if (camera.revision).upper() == "IMX219":
    	try:
		camera.resolution = (3280,2464)
    	except:
		print("Review readme for change in memory split to full support Camera v2")
		print("Resolution kept at 2592x1944")
    		camera.resolution = (2592,1944)
    else: 
	#(camera.revision).upper() == "IMX219":
    	camera.resolution = (2592,1944)
    camera.framerate = Fraction(1, 2)
    camera.iso = 100
    camera.exposure_mode = 'off'
    camera.awb_mode = 'off'
    camera.awb_gains = (1.8,1.8)
    #0.8s exposure
    camera.framerate = 1
    camera.shutter_speed = 800000
    camera.capture('ldr_01.jpg')
    #0.2s exposure
    camera.framerate = 5
    camera.shutter_speed = 200000
    camera.capture('ldr_02.jpg')
    #0.05s exposure
    camera.framerate = 20
    camera.shutter_speed = 50000
    camera.capture('ldr_03.jpg')
    #0.0125s exposure
    camera.framerate = 30
    camera.shutter_speed = 12500
    camera.capture('ldr_04.jpg')
    #0.003125s exposure 
    camera.shutter_speed = 3125
    camera.capture('ldr_05.jpg')
    #0.0008s exposure
    camera.shutter_speed = 800
    camera.capture('ldr_06.jpg')
