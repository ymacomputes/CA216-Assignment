from load_tasks import load_tasks

def schedule_priority_rr(quant):
	# sorting the data into correct order for priority
	tasks = sorted(load_tasks(), key=lambda x: x.priority, reverse=True)
	# counting the amount of passes the loop has done
	passes = 1
	# while true will keep going until all bursts have reached zero
	while True:
		print("passes " + str(passes))
		passes = passes + 1
		# subtract each task's burst by the execution window set (quant)
		for i in range(len(tasks)):
			tasks[i].burst = tasks[i].burst - quant
		# remove tasks that have reached zero without going out of bounds
		x = 0
		y = len(tasks)
		while x < y:
			if tasks[x].burst <= 0:
				tasks.remove(tasks[x])
				y-= 1
			else:
				x += 1
		# printing the tasks
		for t in tasks:
			print(t)
		# stopping the while loop if there are no tasks left
		if not len(tasks):
			break
