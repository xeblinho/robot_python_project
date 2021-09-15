import sys
import zmq
import numpy as np
import os

class DSO(object):
	self.point = ""
	
	# Konstruktor, uruchamia DSO
	def __init__(self):
		self.process = subprocess.run(['rosrun', 'dso_ros dso_live image:=camera/image_raw calib=cameraCalib/camera.txt gamma=cameraCalib/pcalib.txt vignette=cameraCalib/vignetteR.png sampleoutput=1'], 
                         self.stdin=subprocess.PIPE, 
                         universal_newlines=True)
                         
	def __del__(self):
		
	# Subskrybcja topiku na którym DSO wysyła dane
	def connect(self,ip_address):	
		self.contextDSO = zmq.Context()
		self.socketDSO = context.socket(zmq.SUB)
		self.socketDSO.connect ("tcp://"+ip_address+":5556")
		self.socketDSO.setsockopt_string(zmq.SUBSCRIBE, "")
		#print ("Waiting for data...")
	
	# Deparsowanie danych, rozdzielanie i konwersja na float	
	def get_PC_data(self):
		self.point = self.socket.recv()
		self.point = self.point.decode('UTF-8')
		self.point = self.point.split(" ")
		self.point = np.array(self.point))
		return DSOcom()
		
	# Zamykanie DSO
	def close(self):
		self.stdin = '\x03'
		self.process
		
