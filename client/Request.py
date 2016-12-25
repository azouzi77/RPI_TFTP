import socket
import struct
import client.Core
import client.Utils
import client.Resources

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
			request = client.Utils.Structure(client.Resources.WRITE_REQUEST)
			request = request.request_struct(outputfile, client.Resources.OCTAL_MODE)
		elif mode == "get":
			request = client.Utils.Structure(client.Resources.READ_REQUEST)
			request = request.request_struct(input_file, client.Resources.OCTAL_MODE)
		structp = self.struct.pack(*request)
		socket.sendall(structp)
		core = client.Core.Core(socket, input_file, outputfile)
		return