class Task:
	def __init__(self, name, priority, burst):
		self.name = name
		self.priority = priority
		self.burst = burst

	# formatting the string 
	def __str__(self):
		return "{:}: {:} {:}".format(self.name, self.priority, self.burst)

	def __repr__(self):
		return "{:}: {:} {:}".format(self.name, self.priority, self.burst)
