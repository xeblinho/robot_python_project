import sys
import zmq

from robo import Robo
from task import Task
'''
class Main(robo):
	def __init(self):
		
	def __del__(self);
					
	def main(self):
		
		while 1:
			task = Task()
			if task.is_finished():
				break
			'''
if __name__ == "__main__":
	robot = Robo(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	task = Task(robot)
	robot.establish_zmq("5557")
	wait(100)
	while
