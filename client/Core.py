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
		exceed = timer.start_timer()
		ack = None
		if mode == WRITE_REQUEST:
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
		connect = 1
		message_id = -1
		buffer = Utils.FileOpener()
		critical = 0
		file = None
		if mode == READ_REQUEST:
			file = buffer.openfile(self.output_file, 'wb+')
		elif mode == WRITE_REQUEST:
			file = buffer.openfile(self.output_file, 'rb')
		errors = Errors()
		if None == file:
			if mode == READ_REQUEST:
				Get(READ_REQUEST, self.__socket)
				errors.send_error(socket=self.__socket, type="disk", message="Disk full")
				critical = errors.is_critical(0x03, "disk full")
				errors.send_error(self.__socket, "disk full", "disk")
			elif mode == WRITE_REQUEST:
				errors.send_error(socket=self.__socket, type="file", message="File not found")
				critical = errors.is_critical(0x01, "file not found")
				errors.send_error(self.__socket, "File not found", "file")
			self.__socket.close()
			return
		restart = False
		max_exceed = 0
		while (connect):
			if mode == WRITE_REQUEST:
				get = Get(WRITE_REQUEST, self.__socket)
				send = Put(self.__socket)
				if not restart:
					data = file.read(DATA_SIZE, WRITE_REQUEST)
					message_id += 1
				send.send_content(message_id, data)
				try:
					restart = False
					max_exceed = timer.start_timer()
					if -1 == max_exceed:
						break
					get.get_ack()
				except socket.timeout:
					restart = True
			elif mode == READ_REQUEST:
				send = Put(self.__socket)
				get = Get(READ_REQUEST, self.__socket)
				try:
					timer.start_timer()
					data = get.get_content()
				except socket.timeout:
					restart = True
				if not restart:
					message_id += 1
					file.write(data)
				send.send_ack(data)


		self.__socket.close()
		return

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn = sock.connect(('localhost', 20000))
while True:
     try:
             sock.settimeout(5.0)
             buffer, address = conn.recv(516)
     except socket.timeout as timeout:
             print("timeout")
     except socket.error as err:
             print("err")
