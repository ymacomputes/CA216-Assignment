from load_tasks import load_tasks


def fcfs():
	# creating a list for arrival times and turnaround times
	at = []
	tat = []
	tasks = load_tasks()
	# printing the tasks in the order they were given in
	for i in range(len(tasks)):
		task = tasks[i]
		wait_time = 0
		# adding the time of the previous task to the wait time
		for old_task in tasks[:i]:
			wait_time += old_task.burst
		# adding the wait time to arrival time list
		at.append(wait_time)
		# adding the wait wait to the current task's burst time to find the completion time
		completion_time = task.burst + wait_time
		# add the turnaround time (completion time subtract the wait time) to the turnaround list
		tat.append(completion_time - wait_time)
		print(task)
	print("Average wait time " + str(sum(at) / len(at)))
	print("Turnaround time " + str(sum(tat) / len(tat)))


