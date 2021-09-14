import sys
import os

class Camera(object):
	def __init__(self):
		
	def __del__(self):
		
	def open(self):
		self.process = subprocess.run(['roslaunch', 'ueye_cam rgb8.launch'], 
                         self.stdin=subprocess.PIPE, 
                         universal_newlines=True)
    def close(self)
		self.stdin = '\x03'
		self.process = subprocess.run(['roslaunch', 'ueye_cam rgb8.launch'], 
                         self.stdin=subprocess.PIPE, 
                         universal_newlines=True)
	
