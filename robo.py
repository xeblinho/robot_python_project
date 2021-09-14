import sys

import socket
import zmq

from database import Databases as dbs
from dso import DSO
from camera import Camera as cam


class Robo(object):
	def __init__(self, camFlag, dsoFlag, dbpcFlag, dbtagFlag):
		self.camFlag = camFlag
		self.dsoFlag = dsoFlag
		self.dbpcFlag = dbpcFlag
		self.dbtagFlag = dbtagFlag
	
	def establish_zmq(self,port):	
		self.zmqContext = zmq.Context()
		self.zmqSocket = zmqContext.socket(zmq.SUB)
		self.zmqSocket = connect('tcp://192.168.1.1:' + str(port))
		self.zmqSocket.setsockopt(zmq.SUBSCRIBE, "")
		
	def	set_id(self):
		self.ip = self.extract_ip()
		self.id = self.ip.split(".")
		self.id = np.array(self.id)
		zmqSocket.send("roboID %d" % (self.id))
		
	def __del__(self):
		#zamknięcie połączeń, zamknięcie procesów
		
	def extract_ip(self):
		st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:       
			st.connect(('10.255.255.255', 1))
			IP = st.getsockname()[0]
		except Exception:
			IP = '127.0.0.1'
		finally:
			st.close()
		return IP
	
	def initialization(self):
		
		while 1:
			init_param = socket.recv()
			self.topic, self.flag = init_param.split()
			modules = 0
			if not modules == 4:
				match self.topic:
					
					case 'cam':
						self.camFlag = self.flag
						modules += 1
						camera = cam.Camera()
						if self.camFlag:
							camera.open()
							
					case 'dso':
						self.dsoFlag = self.flag
						modules += 1
						if self.dsoFlag == 1:
							odometry = dso.DSO()
							odometry.connect(self.ip)
						if self.dsoFlag == 2:
							odometry = dso.DSO()
							odometry.connect("192.168.1.1")
							
					case 'dbpc':
						self.dbFlag = self.flag
						modules += 1
						if self.dbpcFlag:
							dbpc = dbs.Databases("point_cloud")
							
					case 'dbtag':
						self.dbFlag = self.flag
						modules += 1;
						if self.dbtagFlag:
							dbtag = dbs.Databases("tag_list")
			else:
				break
