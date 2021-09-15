import sys
import zmq

from robo import Robo
from task import Task

# Program główny
if __name__ == "__main__":
	# Tworzenie obiektu klasy Robo z parametrami domyślnymi
	robot = Robo(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	
	# Tworzenie obiektu klasy Task, który zawierać będzie akcje do wykonania
	task = Task(robot)
	
	# Wywołanie metody do ustalenia połączenia z nadzorcą
	robot.establish_zmq("5557")
	wait(100)
	
	# Inicjalizacja systemów
	robot.initialization()
	
	# Po inicjalizacji wszystkie systemy pracują i można rozpocząć wykonywanie zadań
	
	while
