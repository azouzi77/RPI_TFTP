from collections import namedtuple

__author__ = 'Frederick NEY'

from Get import *
from Put import *
from Errors import *
from Timeout import *
import Utils
import socket
from random import randint
from Ressources import *
import struct

class Core:

	__author__ = 'Frederick NEY'

	input_file = None
	output_file = None
	average = 0

	def __init__(self, socket, data, addr, average, path):
		self.__socket = socket
		self.timer = Timeout(5.0, socket)
		data = struct.unpack("!h " + str(len(filename)) + "s c " + str(len(mode)) + "s c", data)
		struct = namedtuple("request_struct", "op_code filename offset_file mode offset_mode")
		struct(data)
		self.mode = struct.mode
		self.filename = struct.filename
		self.request = struct.op_code
		self.address = addr[0]
		self.average = average
		self.path = path
		self.port = addr[1]
		return

	def GetAnswer(self):
		buffer = Utils.FileOpener()
		send = Put(self.__socket, self.address, self.port)
		errors = Errors(self.address, self.port)
		data_rec = Structure(self.request)
		file = None
		blk_num = 0
		if self.mode == WRITE_REQUEST:
			send.send_ack(0)
			file = buffer.openfile(self.filename, 'wb+')
		else:
			file = buffer.openfile(self.filename, 'rb')
		if not file:
			if self.mode == WRITE_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           access violation                                       """
				"""--------------------------------------------------------------------------------------------------"""
				self.__send__error__(0x02, errors, "access violation")
			if self.mode == READ_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           file not found                                         """
				"""--------------------------------------------------------------------------------------------------"""
				self.__send__error__(0x01, errors, "unable to read file : " + self.filename)
		restart = False
		while connect:
			recv = Get(self.mode, self.__socket, self.address, self.port)
			if self.mode == READ_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           send file                                              """
				"""--------------------------------------------------------------------------------------------------"""
				if not restart:
					blk = buffer.readfile()
					blk_num += 1
				data, addr = self.__socket.recvfrom(PACKET_SIZE)
				opcode = struct.unpack("!h", data[0:2])[0]
				if opcode == READ_REQUEST:
					"""----------------------------------------------------------------------------------------------"""
					"""                                         resend ack                                           """
					"""----------------------------------------------------------------------------------------------"""
					send.send_content(blk_num, blk)
					restart = True
				elif opcode == ACK:
					"""----------------------------------------------------------------------------------------------"""
					"""                                        send next block                                       """
					"""----------------------------------------------------------------------------------------------"""
					send.send_content(blk_num, blk)
					structure = data_rec.get_ack_struct(data)
					if structure.block == blk_num:
						"""------------------------------------------------------------------------------------------"""
						"""                                      block matching                                      """
						"""------------------------------------------------------------------------------------------"""
						restart = False
					else:
						"""------------------------------------------------------------------------------------------"""
						"""                                      block not matching                                  """
						"""------------------------------------------------------------------------------------------"""
						file.close()
						buffer.openfile(self.filename, 'rb')
						self.__read_file__(buffer, structure.block)
						restart = False
				else:
					restart = True
			elif self.mode == WRITE_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           recv file                                              """
				"""--------------------------------------------------------------------------------------------------"""
				data, addr = self.__socket.recvfrom(PACKET_SIZE)
				opcode = struct.unpack("!h", data[0:2])[0]
				if opcode == WRITE_REQUEST:
					"""----------------------------------------------------------------------------------------------"""
					"""                                         resend ack                                           """
					"""----------------------------------------------------------------------------------------------"""
					send.send_ack(0)
				elif opcode == DATA:
					"""----------------------------------------------------------------------------------------------"""
					"""                                       recv next data                                         """
					"""----------------------------------------------------------------------------------------------"""
					structure = data_rec.get_data_struct(data)
					if structure.block == blk_num:
						"""------------------------------------------------------------------------------------------"""
						"""                                      block matching                                      """
						"""------------------------------------------------------------------------------------------"""
						buffer.writefile(structure.data)
						blk_num += 1
					else:
						"""------------------------------------------------------------------------------------------"""
						"""                                      block not matching                                  """
						"""------------------------------------------------------------------------------------------"""
						self.__send__error__(0x04, errors, "wrong block id for file: " + self.filename)
				else:
					"""----------------------------------------------------------------------------------------------"""
					"""                                          other error                                         """
					"""----------------------------------------------------------------------------------------------"""
					self.__send__error__(0x05, errors, "Operation not permitted :" + self.mode)
			else:
				self.__send__error__(0x05, errors, "Operation not permitted :" + self.mode)
		return

	def __read_file__(self, buffer, blk_num):
		for n in range(1, blk_num):
			buffer = buffer.readfile()
		return

	def __send__error__(self, error_id, errors, message):
		critical = False
		if error_id == 0x03:
			errors.send_error(socket=self.__socket, type="disk", message=message)
			critical = errors.is_critical(error_id, "disk full")
		elif error_id == 0x01:
			errors.send_error(socket=self.__socket, type="file", message=message)
			critical = errors.is_critical(error_id, "file not found")
		elif error_id == 0x04:
			errors.send_error(socket=self.__socket, type="id", message=message)
		elif error_id == 0x02:
			errors.send_error(socket=self.__socket, type="acces", message=message)
			critical = errors.is_critical(error_id, "access violation")
		return critical