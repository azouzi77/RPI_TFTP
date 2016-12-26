__author__ = 'Frederick NEY'

from client.Get import *
from client.Put import *
from client.Errors import *
from client.Timeout import *
from client import Resources, Utils
import socket
from random import randint


class Core:

	__author__ = 'Frederick NEY'

	input_file = None
	output_file = None
	average = 0

	def __init__(self, socket, input_file, output_file, request_packed, average, timer):
		self.__socket = socket
		self.input_file = input_file
		self.output_file = output_file
		self.request_packed = request_packed
		self.average = average
		self.timer = Timeout(5.0, timer)
		return

	def GetAnswer(self, mode):
		"""
		if rand > average then send
		else do not send
		"""
		recv = Get(mode, self.__socket)
		timeout = True
		timer = Timeout(5.0, self.timer)
		ack = None
		connect = 1
		message_id = -1
		buffer = Utils.FileOpener()
		file = False
		if mode == READ_REQUEST:
			mode = 0x03
			file = buffer.openfile(self.output_file, 'wb+')
		elif mode == WRITE_REQUEST:
			mode = 0x01
			exceed = timer.start_timer()
			while timeout:
				timeout = False
				try:
					ack = recv.get_ack()
				except socket.timeout:
					timeout = True
					exceed = timer.restart_timer()
					if exceed == -1:
						break
			if ack != None and recv.error == 1:
				self.__socket.close()
				return
			if -1 == exceed:
				self.__socket.close()
				return
			timer.cancel_timer()
			file = buffer.openfile(self.output_file, 'rb')
		errors = Errors()
		if not file:
			self.__send__error__(mode, errors)
			self.__socket.close()
			return
		restart = False
		max_exceed = 0
		error_uncritical = 0
		while (connect):

			if mode == 0x01:
				""" send file """
				get = Get(WRITE_REQUEST, self.__socket)
				send = Put(self.__socket)
				if not restart:
					data = buffer.readfile()
					message_id += 1
				send.send_content(message_id, data)
				try:
					restart = False
					if 0 == error_uncritical:
						max_exceed = timer.start_timer()
					if -1 == max_exceed:
						break
					reply = get.get_ack()
					if len(reply) == 2:
						if errors.is_critical(reply[0], reply[1]):
							errors.print_error()
							break
						else:
							restart = True
							error_uncritical = 1
							max_exceed = timer.restart_timer()
					else:
						error_uncritical = 0
				except socket.timeout:
					restart = True
			elif mode == 0x03:
				""" get file """
				send = Put(self.__socket)
				get = Get(READ_REQUEST, self.__socket)
				try:
					max_exceed = timer.start_timer()
					reply = get.get_content()
					if get.error:
						if errors.is_critical(reply[0], reply[1]):
							errors.print_error()
							break
						else:
							restart = True
							error_uncritical = 1
							max_exceed = timer.restart_timer()
					else:
						error_uncritical = 0
				except socket.timeout:
					restart = True
				if not restart:
					message_id += 1
					buffer.writefile(data)
				send.send_ack(data)
		self.__socket.close()
		return

	def __send__error__(self, mode, errors, message):
		critical = False
		if mode == 0x03:
			errors.send_error(socket=self.__socket, type="disk", message=message)
			critical = errors.is_critical(0x03, "disk full")
			errors.send_error(self.__socket, "disk full", "disk")
		elif mode == 0x01:
			errors.send_error(socket=self.__socket, type="file", message=message)
			critical = errors.is_critical(0x01, "file not found")
			errors.send_error(self.__socket, "File not found", "file")
		elif mode == 0x04:
			errors.send_error(socket=self.__socket, type="id", message=message)
		return critical