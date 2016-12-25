__author__ = 'Frederick NEY'

from struct import Struct
from collections import namedtuple


class FileOpener:

	__author__ = 'Frederick NEY'

	def openfile(self, filename, mode):
		try:
			return open(filename, mode=mode)
		except IOError:
			return None


class Structure:

	OpCode = None

	def __init__(self, op_code):
		self.OpCode = op_code
		return

	def data_struct(self, block, data):
		struct = namedtuple("data_struct", "op_code block data offset")
		struct_handle = Struct("!h h " + str(len(data)) + "s c")
		return struct_handle.pack(*struct(self.OpCode,  block, data, b'\0'))

	def request_struct(self, filename, mode):
		struct = namedtuple("request_struct", "op_code filename offset_file mode offset_mode")
		struct_handle = Struct("!h " + str(len(filename)) + "s c " + str(len(mode)) + "s c")
		return struct_handle.pack(*struct(self.OpCode, filename, b'\0',  mode, b'\0'))

	def ack_struct(self, block):
		struct = namedtuple("ack_struct", "op_code block")
		return struct(self.OpCode, block)

	def error_struct(self, error_code, error_message):
		struct = namedtuple("error_struct", "op_code error_code error_message offset")
		struct_handle = Struct("!h h " + str(len(error_message)) + "s c")
		return struct_handle.pack(*struct(self.OpCode, error_code, error_message, b'\0'))

