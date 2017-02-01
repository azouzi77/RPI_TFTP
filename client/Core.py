__author__ = 'Frederick NEY'

from Get import *
from Put import *
from Errors import *
from Timeout import *
import Utils
import socket
from random import randint


class Core:

	__author__ = 'Frederick NEY'

	input_file = None
	output_file = None
	average = 0

	def __init__(self, socket, input_file, output_file, request_packed, average, timer, address, port):
		self.__socket = socket
		self.input_file = input_file
		self.output_file = output_file
		self.request_packed = request_packed
		self.average = average
		self.timer = Timeout(5.0, timer)
		self.address = address
		self.port = port
		return

	def GetAnswer(self, mode):
		recv = Get(mode, self.__socket, self.address, self.port)
		timeout = True
		timer = self.timer
		reply = None
		connect = True
		message_id = -1
		buffer = Utils.FileOpener()
		errors = Errors(self.address, self.port)
		file = False
		if mode == READ_REQUEST:
			mode = 0x03
			file = buffer.openfile(self.output_file, 'wb+')
			if None == file:
				self.__send__error__(0x02, errors, "access violation")
		elif mode == WRITE_REQUEST:
			mode = 0x01
			message_id = 0
			while timeout:
				timeout = False
				try:
					exceed = timer.start_timer()
					if exceed == -1:
						self.__socket.close()
						print("no ack for write request received")
						return
					reply = recv.get_ack()
					if type(reply) is tuple:
						if errors.is_critical(reply[0], reply[1]):
							errors.print_error()
							timer.cancel_timer()
							self.__socket.close()
							return
						else:
							errors.print_error()
							timeout = True
							timer.cancel_timer()
				except socket.timeout:
					rand = randint(0, 100)
					if rand >= self.average:
						self.__socket.sendto(self.request_packed, (self.address, self.port))
					timeout = True
			file = buffer.openfile(self.input_file, 'rb')
			if None == file:
				self.__send__error__(0x01, errors, "file not found")
		if None == file:
			self.__socket.close()
			return
		restart = False
		while connect:
			if mode == 0x01:
				""" send file """
				get = Get(WRITE_REQUEST, self.__socket, self.address, self.port)
				send = Put(self.__socket, self.address, self.port)
				if not restart:
					data = buffer.readfile()
					message_id += 1
				rand = randint(0, 100)
				if rand >= self.average:
					send.send_content(message_id, data)
				if len(data) < DATA_SIZE:
					connect = False
				try:
					restart = False
					max_exceed = timer.start_timer()
					if -1 == max_exceed:
						print("connection lost")
						break
					reply = get.get_ack()
					if type(reply) is tuple:
						if errors.is_critical(reply[0], reply[1]):
							errors.print_error()
							break
						else:
							restart = True
							max_exceed = timer.restart_timer()
							if -1 == max_exceed:
								print("connection lost")
								break
							self.__send__error__(0x04, errors, "id invalid " + str(reply[0]))
							errors.print_error()
							connect = True
					else:
						timer.cancel_timer()
						if reply != message_id:
							self.__send__error__(0x04, errors, "invalid id" + str(reply))
							errors.print_error()
							connect = True
							restart = True
				except socket.timeout:
					connect = True
					restart = True
			elif mode == 0x03:
				""" get file """
				send = Put(self.__socket, self.address, self.port)
				get = Get(READ_REQUEST, self.__socket, self.address, self.port)
				try:
					max_exceed = timer.start_timer()
					if -1 == max_exceed:
						print("connection lost")
						break
					reply = get.get_content()
					if get.error:
						if errors.is_critical(reply[0], reply[1]):
							errors.print_error()
							break
						else:
							restart = True
							max_exceed = timer.restart_timer()
							if -1 == max_exceed:
								print("connection lost")
								break
					else:
						if len(reply[1]) < DATA_SIZE:
							connect = False
						timer.cancel_timer()
						if buffer.writefile(reply[1]) < len(reply[1]):
							self.__send__error__(0x03, errors, "disk full")
							break
				except socket.timeout:
					restart = True
				if not restart:
					message_id += 1
				rand = randint(0, 100)
				if message_id == 0 and restart:
					if rand >= self.average:
						self.__socket.sendto(self.request_packed, (self.address, self.port))
				else:
					if rand >= self.average:
						send.send_ack(message_id)
				if not connect:
					final_ack = False
					while not final_ack:
						try:
							exceed = timer.start_timer()
							if exceed == -1:
								break
							content = recv.get_content()
							rand = randint(0, 100)
							if rand >= self.average:
								send.send_ack(message_id)
						except socket.timeout:
							final_ack = True
		self.__socket.close()
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