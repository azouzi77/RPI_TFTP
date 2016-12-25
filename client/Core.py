__author__ = 'Frederick NEY'

from client import Get, Put, Ressources, Utils, Error
import socket

class Core:

	__author__ = 'Frederick NEY'

	input_file = None
	output_file = None

	def __init__(self, socket, input_file, output_file):
		self.__socket = socket
		self.input_file = input_file
		self.output_file = output_file
		return

	def GetAnswer(self, mode):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect()
		connect = 1
		message_id = 1
		buffer = Utils.FileOpener()
		critical = 0
		if mode == READ_REQUEST:
			file = buffer.openfile(self.output_file, 'w+')
		elif mode == WRITE_REQUEST:
			file = buffer.openfile(self.output_file, 'r')

		while (connect):
			if None == file:
				if mode == READ_REQUEST:
					Error.SendError(message="Disk full")
					critical = Error.IsCritical("disk")
				elif mode == WRITE_REQUEST:
					Error.SendError(message="File not found")
					critical = Error.IsCritical("file")
			else:
				if mode = WRITE_REQUEST:
					data = file.read(DATA_SIZE)
					data
			message_id += 1
		return