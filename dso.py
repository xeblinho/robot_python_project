import sys
import zmq
import numpy as np
import os

class DSO(object):
	self.point = ""
	def __init__(self):
		self.process = subprocess.run(['rosrun', 'dso_ros dso_live image:=camera/image_raw calib=cameraCalib/camera.txt gamma=cameraCalib/pcalib.txt vignette=cameraCalib/vignetteR.png sampleoutput=1'], 
                         self.stdin=subprocess.PIPE, 
                         universal_newlines=True)
        self.process
	def __del__(self):
		
	def connect(self,ip_address):	
		self.contextDSO = zmq.Context()
		self.socketDSO = context.socket(zmq.SUB)
		self.socketDSO.connect ("tcp://"+ip_address+":5556")
		self.socketDSO.setsockopt_string(zmq.SUBSCRIBE, "")
		print ("Waiting for data...")
		
	def get_PC_data(self):
		self.point = self.socket.recv()
		self.point = self.point.decode('UTF-8')
		self.point = self.point.split(" ")
		self.point = np.array(self.point))
		return DSOcom()

	def close(self):
		self.stdin = '\x03'
		self.process
		
