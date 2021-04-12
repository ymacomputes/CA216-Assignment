from Task import Task
import sys

def load_tasks():
	# reading in the filename and creating a list for the tasks
	filename = sys.argv[1]
	tasks = []
	# opening the file
	with open(filename) as f:
		# read in the all the lines
		lines = f.readlines()
		# looping through the list to split each task into another list of the name, priority and burst
		for line in lines:
			line = line.split(", ")
			# construct an instance of the task class
			try:
				tasks.append(Task(line[0], int(line[1]), int(line[2])))
			# errorchecking for when someone tries to convert a character into an integer
			except ValueError:
				print("You tried to convert a character into an integer")
	return tasks
