from time import sleep
from picamera import PiCamera




def Capture(name):
    camera.capture(name)

camera = PiCamera()
camera.resolution = (1024, 786)

