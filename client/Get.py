#__author__ = 'Stephan OVERLEN'

import binascii
import socket
import struct
import sys

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

	def data_get(self):
	    data = self.soket.recv(structData.size)
            unpacked_data = structData.unpack(data)                 # get unpacked data
            if unpacked_data[0] == 0x03:                            # data packet
                error = False
            else:                                                   # error packet
                error = True
            return unpacked_data[1:2]                               # [blocNum, content]

	def get_ack(self):
	    data = self.soket.recv(structAck.size)
            unpacked_data = structData.unpack(data)                 # get unpacked data
            return unpacked_data[1]
