__author__ = 'admin_master'
import client.Utils
import client.Resources


class Errors:

	__error_not_defined__ = 0x00
	__file_not_found__ = 0x01
	__access_violation__ = 0x02
	__disk_full__ = 0x03
	__id_error__ = 0x04
	__illegal_operation__ = 0x05
	__file_exist__ = 0x06
	handle = None
	error = 0

	def __init__(self):
		return

	def send_error(self, socket, message, type):
		error_struct = client.Utils.Structure(client.Resources.ERROR)
		if type == "acces":
			socket.sendall(error_struct.error_struct(self.__access_violation__, message))
			return
		elif type == "file":
			socket.sendall(error_struct.error_struct(self.__file_not_found__, message))
			return
		elif type == "disk":
			socket.sendall(error_struct.error_struct(self.__disk_full__, message))
			return
		elif type == "id":
			socket.sendall(error_struct.error_struct(self.__id_error__, message))
			return
		elif type == "operation":
			socket.sendall(error_struct.error_struct(self.__illegal_operation__, message))
			return
		elif type == "exist":
			socket.sendall(error_struct.error_struct(self.__file_exist__, message))
			return
		else:
			socket.sendall(error_struct.error_struct(self.__error_not_defined__, message))
			return

	def is_critical(self, error, handle):
		self.handle = handle
		if error == self.__error_not_defined__:
			self.error = 1
		elif error == self.__access_violation__:
			self.error = 1
		elif error == self.__disk_full__:
			self.error = 1
		elif error == self.__id_error__:
			self.error = 0
		elif error == self.__illegal_operation__:
			self.error = 1
		elif error == self.__file_exist__:
			self.error = 1
		return self.error

	def print_error(self):
		print(self.handle)