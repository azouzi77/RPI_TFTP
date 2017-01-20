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
		connect = True
		filename = self.filename.split('/')
		if 1 == len(filname):
			self.filename = filename[0]
		else:
			self.__send__error__(0x02, errors, "access violation")
			connect = False
		if self.request == WRITE_REQUEST:
			send.send_ack(0)
			file = buffer.openfile(self.path + self.filename, 'wb+')
		elif self.request == READ_REQUEST:
			file = buffer.openfile(self.path + self.filename, 'rb')
		if not file:
			if self.mode == WRITE_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           access violation                                       """
				"""--------------------------------------------------------------------------------------------------"""
				self.__send__error__(0x02, errors, "access violation")
				connect = False
			if self.mode == READ_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           file not found                                         """
				"""--------------------------------------------------------------------------------------------------"""
				self.__send__error__(0x01, errors, "unable to read file : " + self.filename)
				connect = False
		restart = False
		write_err = False
		opcode = 0x04
		init = False
		while connect:
			init = False
			recv = Get(self.mode, self.__socket, self.address, self.port)
			if self.request == READ_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           send file                                              """
				"""--------------------------------------------------------------------------------------------------"""
				if not restart and opcode == ACK:
					blk = buffer.readfile()
					blk_num += 1
				if opcode == READ_REQUEST and blk_num == 1:
					"""----------------------------------------------------------------------------------------------"""
					"""                                         resend init ack                                      """
					"""----------------------------------------------------------------------------------------------"""
					rand = randint(0, 100)
					if rand > self.average:
						send.send_content(blk_num, blk)
					init = True
					data, addr = self.__socket.recvfrom(PACKET_SIZE)
					self.port = addr[1]
					send.port = addr[1]
					opcode = struct.unpack("!h", data[0:2])[0]
				if opcode == ACK and not init:
					"""----------------------------------------------------------------------------------------------"""
					"""                                        send next block or lost block                         """
					"""----------------------------------------------------------------------------------------------"""
					rand = randint(0, 100)
					if rand > self.average or blk < DATA_SIZE:
						send.send_content(blk_num, blk)
						restart = False
					else:
						restart = True
					"""----------------------------------------------------------------------------------------------"""
					"""                                        recv ack                                              """
					"""----------------------------------------------------------------------------------------------"""
					data, addr = self.__socket.recvfrom(PACKET_SIZE)
					self.port = addr[1]
					send.port = addr[1]
					opcode = struct.unpack("!h", data[0:2])[0]
					structure = data_rec.get_ack_struct(data)
					if structure.block == blk_num:
						"""------------------------------------------------------------------------------------------"""
						"""                                      block matching                                      """
						"""------------------------------------------------------------------------------------------"""
						restart = False
					elif structure.block > blk_num:
						"""------------------------------------------------------------------------------------------"""
						"""                                      block not matching                                  """
						"""------------------------------------------------------------------------------------------"""
						rand = randint(0, 100)
						if rand > self.average:
							self.__send__error__(0x04, errors, 'invalid id : ' + structure.block)
						restart = True
					else:
						restart = True
				else:
					restart = True
				if blk < DATA_SIZE:
					timer = Timeout(5.0, self.__socket)
					"""----------------------------------------------------------------------------------------------"""
					"""                                       final blk                                              """
					"""----------------------------------------------------------------------------------------------"""
					while connect:
						try:
							max_exceed = timer.start_timer()
							if -1 == max_exceed:
								print("closing connection")
								connect = False
							else:
								data, addr = self.__socket.recvfrom(PACKET_SIZE)
								opcode = struct.unpack("!h", data[0:2])[0]
								if opcode == READ_REQUEST or opcode == WRITE_REQUEST:
									return (data, addr)
								else:
									send.send_content(blk_num, blk)
									connect = True
						except socket.timeout:
							connect = False
			elif self.request == WRITE_REQUEST:
				"""--------------------------------------------------------------------------------------------------"""
				"""                                           recv file                                              """
				"""--------------------------------------------------------------------------------------------------"""
				data, addr = self.__socket.recvfrom(PACKET_SIZE)
				self.port = addr[1]
				send.port = addr[1]
				opcode = struct.unpack("!h", data[0:2])[0]
				if opcode == WRITE_REQUEST and blk_num == 0:
					"""----------------------------------------------------------------------------------------------"""
					"""                                         resend ack                                           """
					"""----------------------------------------------------------------------------------------------"""
					send.send_ack(0)
				elif opcode == DATA:
					"""----------------------------------------------------------------------------------------------"""
					"""                                       recv next data                                         """
					"""----------------------------------------------------------------------------------------------"""
					structure = data_rec.get_data_struct(data)
					if structure.block == blk_num + 1:
						self.port = addr[1]
						"""------------------------------------------------------------------------------------------"""
						"""                                      block matching                                      """
						"""------------------------------------------------------------------------------------------"""
						if not restart:
							write = buffer.writefile(structure.data)
							if write < len(structure.data):
								self.__send__error__(0x03, errors, "disk full")
								connect = False
								write_err = True
							else:
								write_err = False
						blk_num += 1
						rand = randint(0, 100)
						if rand > self.average or len(structure.data) < DATA_SIZE:
							if not write_err:
								send.port = addr[1]
								send.send_ack(structure.block)
							restart = False
						else:
							rand = randint(0, 100)
							if rand > self.average:
								self.__send__error__(0x04, errors, "invalid transfer id : " + structure.block)
							restart = True
					else:
						"""------------------------------------------------------------------------------------------"""
						"""                                      block not matching                                  """
						"""------------------------------------------------------------------------------------------"""
						self.__send__error__(0x04, errors, "wrong block id for file: " + self.filename)
						restart = True
				else:
					"""----------------------------------------------------------------------------------------------"""
					"""                                          other error                                         """
					"""----------------------------------------------------------------------------------------------"""
					self.__send__error__(0x05, errors, "Operation not permitted during transfer:" + opcode)
					connect = False
				if structure.block < PACKET_SIZE and opcode == DATA:
					"""----------------------------------------------------------------------------------------------"""
					"""                                       final ack                                              """
					"""----------------------------------------------------------------------------------------------"""
					while connect:
						try:
							max_exceed = timer.start_timer()
							if -1 == max_exceed:
								print("closing connection")
								connect = False
							else:
								data, addr = self.__socket.recvfrom()
								opcode = struct.unpack("!h", data[0:2])[0]
								if opcode == READ_REQUEST or opcode == WRITE_REQUEST:
									return (data, addr)
								else:
									send.send_ack(blk_num)
									connect = True
						except socket.timeout:
							connect = False
			else:
				self.__send__error__(0x05, errors, "Operation not permitted :" + self.request)
				connect = False
		return None, None

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