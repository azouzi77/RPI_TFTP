__author__ = 'Frederick NEY'

from struct import Struct
import struct
from collections import namedtuple


class FileOpener:

	__author__ = 'Frederick NEY'
	descriptor = None

	def openfile(self, filename, mode):
		try:
			self.descriptor = open(filename, mode=mode)
			file = True
		except IOError:
			file = False
		return file

	def readfile(self):
		return self.descriptor.read(512)

	def writefile(self, data):
		try:
			write = self.descriptor.write(data)
			self.descriptor.flush()
		except OSError:
			write = -1
		return write


class Structure:

	OpCode = None

	def __init__(self, op_code):
		self.OpCode = op_code
		return

	def data_struct(self, block, data):
		struct = namedtuple("data_struct", "op_code block data offset")
		struct_handle = Struct("!h h " + str(len(data)) + "s")
		data = data.encode('utf-8')
		return struct_handle.pack(*struct(self.OpCode,  block, data))

	def request_struct(self, filename, mode):
		struct = namedtuple("request_struct", "op_code filename offset_file mode offset_mode")
		filename = filename.encode('utf-8')
		mode = mode.encode("utf-8")
		struct_handle = Struct("!h " + str(len(filename)) + "s c " + str(len(mode)) + "s c")
		return struct_handle.pack(*struct(self.OpCode, filename, b'\0',  mode, b'\0'))

	def ack_struct(self, block):
		struct = namedtuple("ack_struct", "op_code block")
		struct_handle = Struct("!h h")
		return struct_handle.pack(*struct(self.OpCode, block))

	def error_struct(self, error_code, error_message):
		struct = namedtuple("error_struct", "op_code error_code error_message offset")
		error_message = error_message.encode('utf-8')
		struct_handle = Struct("!h h " + str(len(error_message)) + "s c")
		return struct_handle.pack(*struct(self.OpCode, error_code, error_message, b'\0'))

	def get_data_struct(self, struct_recv):
		struct_handle = namedtuple("data_struct", "op_code block data offset")
		struct_unpack = Struct("!h h " + str(len(struct_recv) - 4) + "s", struct_recv)
		return struct_handle(struct_unpack[0], struct_unpack[1], struct_unpack[2].decode())

	def get_request_struct(self, struct_recv):
		struct_handle = namedtuple("request_struct", "op_code filename offset_file mode offset_mode")
		struct_unpack = struct.unpack("!h " + str(len(struct_recv) - 9) + "s c 5s c", struct_recv)
		return struct_handle(struct_unpack[0], struct_unpack[1].decode(), struct_unpack[2].decode(), struct_unpack[3].decode(), struct_unpack[4].decode())

	def get_ack_struct(self, struct_recv):
		struct_handle = namedtuple("ack_struct", "op_code block")
		struct_unpack = struct.unpack("!h h", struct_recv)
		return struct_handle(struct_unpack[0], struct_unpack[1])

	def get_error_struct(self, struct_recv):
		struct_handle = namedtuple("error_struct", "op_code error_code error_message offset")
		struct_unpack = struct.unpack("!h h " + str(len(struct_recv) - 5) + "s c")
		return struct_handle(struct_unpack[0], struct_unpack[1], struct_unpack[2].decode(), struct_unpack[3].decode())