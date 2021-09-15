import sys
import os

class Camera(object):
	def __init__(self):
		
	def __del__(self):
		
	# Rozpoczęcie akwizycji oraz transmisji
	def open(self):
		self.process = subprocess.run(['roslaunch', 'ueye_cam rgb8.launch'], 
                         self.stdin=subprocess.PIPE, 
                         universal_newlines=True)
    # Zakończenie akwizycji i zamknięcie komunikacji
    def close(self):
		self.stdin = '\x03'
		self.process = subprocess.run(['roslaunch', 'ueye_cam rgb8.launch'], 
                         self.stdin=subprocess.PIPE, 
                         universal_newlines=True)
	
