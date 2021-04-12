from schedule_fcfs import fcfs as fcfs
from schedule_sjf import schedule_sjf as sjf
from schedule_priority import priority as priority
from schedule_rr import schedule_rr as round_robin
from schedule_priority_rr import schedule_priority_rr as round_robin_priority

if __name__ == "__main__":
	print("fcfs")
	fcfs()
	print("sjf")
	sjf()
	print("priority")
	priority()
	print("round robin")
	round_robin(10)
	print("round robin priority")
	round_robin_priority(10)
