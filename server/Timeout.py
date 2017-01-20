__author__ = 'Frederick NEY'
from random import randint


class Timeout:

	max_timeout_exeeded = 0
	count_timeout = 0
	seconds = 0

	def __init__(self, seconds, timer):
		self.max_timeout_exeeded = randint(10, 15)
		self.count_timeout = 0
		self.seconds = seconds
		self.timer = timer

	def start_timer(self):
		if self.count_timeout == self.max_timeout_exeeded:
			return -1
		else:
			self.count_timeout += 1
			self.timer.settimeout(self.seconds)
			return 0

	def restart_timer(self):
		if self.count_timeout == self.max_timeout_exeeded:
			return -1
		else:
			self.timer.settimeout(None)
			self.count_timeout += 1
			self.timer.settimeout(self.seconds)
			return 0

	def cancel_timer(self):
		self.timer.settimeout(None)
		self.count_timeout = 0
