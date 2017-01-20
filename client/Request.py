from Core import *
from Get import *
import Utils
import Resources
from random import randint
import socket
import struct
import sys

__author__ = 'Frederick NEY'


class Request:

	def __init__(self, hostname, port, average):
		self.hostname = hostname
		self.port = int(port)
		self.average = int(average)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.struct = struct.Struct("!h h 5s")
		return

	def request_connection(self, input_file, outputfile, mode):
		socket = self.socket
		request = None
		if mode == "put":
			mode = Resources.WRITE_REQUEST
			request = Utils.Structure(Resources.WRITE_REQUEST)
			request = request.request_struct(outputfile, Resources.OCTAL_MODE)
		elif mode == "get":
			mode = Resources.READ_REQUEST
			request = Utils.Structure(Resources.READ_REQUEST)
			request = request.request_struct(input_file, Resources.OCTAL_MODE)
		struct_packed = request
		rand = randint(0, 100)
		if rand >= self.average:
			socket.sendto(struct_packed, (self.hostname, self.port))
		core = Core(socket, input_file, outputfile, struct_packed, self.average, self.socket, address=self.hostname, port=self.port)
		core.GetAnswer(mode)
		return