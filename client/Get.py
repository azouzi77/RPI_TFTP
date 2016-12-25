#__author__ = 'Stephan OVERLEN'

import binascii
import socket
import struct
from client.Resources import *
import client.Utils

structSend = struct.Struct('!h 7s h 5s h')
structData = struct.Struct('!h h 512s')
structAck = struct.Struct('!h h')
blocNum = 0

class Get:

	op_code = None
	error = 0
	socket = None

	def __init__(self, opcode, socket):
		self.op_code = opcode
		self.socket = socket

	def get_content(self):
		data = self.socket.recv(structData.size)
		unpacked_data = structData.unpack(data)                 # get unpacked data
		if unpacked_data[0] == DATA:                            # data packet
			self.error = False
		else:                                                   # error packet
			self.error = True
		return unpacked_data[1:2]                               # [blocNum, content]

	def get_ack(self):
		data = self.socket.recv(structAck.size)
		unpacked_data = structData.unpack(data)                 # get unpacked data
		return unpacked_data[1]
