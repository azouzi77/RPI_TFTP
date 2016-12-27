from client.Core import *
from client.Timeout import *
from client.Get import *
import client.Utils
import client.Resources
from random import randint
import socket
import struct

__author__ = 'Frederick NEY'


class Request:

	def __init__(self, hostname, port, average):
		self.hostname = hostname
		self.port = port
		self.average = average
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.struct = struct.Struct("!h h 5s")
		return

	def request_connection(self, input_file, outputfile, mode):
		socket = self.socket.connect((self.hostname, self.port))
		request = None
		if mode == "put":
			mode = client.Resources.WRITE_REQUEST
			request = client.Utils.Structure(client.Resources.WRITE_REQUEST)
			request = request.request_struct(outputfile, client.Resources.OCTAL_MODE)
		elif mode == "get":
			mode = client.Resources.READ_REQUEST
			request = client.Utils.Structure(client.Resources.READ_REQUEST)
			request = request.request_struct(input_file, client.Resources.OCTAL_MODE)
		struct_packed = self.struct.pack(*request)
		rand = randint(0, 100)
		if rand >= self.average:
			socket.sendall(struct_packed)
		core = Core(socket, input_file, outputfile, struct_packed, self.average, self.socket)
		core.GetAnswer(mode)
		return