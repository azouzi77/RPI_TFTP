#__author__ = 'Stephan OVERLEN'

import socket
import struct
from Resources import *


class Get:

	op_code = None
	error = 0
	socket = None

	def __init__(self, opcode, socket, address, port):
		self.op_code = opcode
		self.socket = socket
		self.address = address
		self.port = port

	def get_content(self):
		data, addr = self.socket.recvfrom(PACKET_SIZE)
		print(data)
		print(len(data))
		data_struct = struct.Struct("!h h " + str(len(data) - 4) + "s")
		unpacked_data = data_struct.unpack(data)                 # get unpacked data
		if unpacked_data[0] == DATA:                            # data packet
			self.error = False
		else:                                                   # error packet
			self.error = True
		return unpacked_data[1:3]                               # [blocNum, content]

	def get_ack(self):
		data, addr = self.socket.recvfrom(PACKET_SIZE)
		if len(data) == 4:
			ack_struct = struct.Struct("!h h")
		else:
			ack_struct = struct.Struct("!h h " + str(len(data) - 5) + "s c")
		unpacked_data = ack_struct.unpack(data)                 # get unpacked data
		if unpacked_data[0] == ACK:                            # data packet
			self.error = False
			return unpacked_data[1]
		else:                                                   # error packet
			self.error = True
			return unpacked_data[1:3]
