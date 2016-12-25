#__author__ = 'Stephan OVERLEN'

import binascii
import socket
import struct
from client.Resources import *
import client.Utils


class Get:

	op_code = None
	error = 0
	socket = None

	def __init__(self, opcode, socket):
		self.op_code = opcode
		self.socket = socket

	def get_content(self):
		data = self.socket.recv(client.Resources.PACKET_SIZE)
		data_struct = struct.Struct("!h h " + str(len(data) - 3) + "s c")
		unpacked_data = data_struct.unpack(data)                 # get unpacked data
		if unpacked_data[0] == DATA:                            # data packet
			self.error = False
		else:                                                   # error packet
			self.error = True
		return unpacked_data[1:2]                               # [blocNum, content]

	def get_ack(self):
		data = self.socket.recv(4)
		ack_struct = struct.Struct("!h h")
		unpacked_data = ack_struct.unpack(data)                 # get unpacked data
		return unpacked_data[1]
