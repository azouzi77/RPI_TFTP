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
		return struct(self.OpCode, block, data)

	def request_struct(self, filename, mode):
		struct = namedtuple("request_struct", "op_code filename offset mode offset")
		return struct(self.OpCode, filename, 0x0,  mode, 0x0)

	def ack_struct(self, block):
		struct = namedtuple("ack_struct", "op_code block")
		return struct(self.OpCode, block)

	def error_struct(self, error_code, error_message):
		struct = namedtuple("error_struct", "op_code error_code error_message")
		return struct(self.OpCode, error_code, error_message)

	def struct_format(self, format, pack=1):
		packed = '!'
		if 1 == pack:
			format = packed + format
		return Struct(format)
