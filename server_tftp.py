"""
TFTP Server
"""
import socket
import sys
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
content = 'qwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertzqwertz'
blocNum = 0x00
structReceived = struct.Struct('!h 7s h 5s h')
structData = struct.Struct('!h h 512s')
structAck = struct.Struct('!h h')

server_address = ('localhost', 10000)
print >>sys.stderr, 'Starting up on %s port %s' % server_address

sock.bind(server_address)                                       # bind
sock.listen(1)                                                  #listen

while True:
    print >>sys.stderr, 'waiting for a connection'
    
    try:
        print 'accept connection:'
        connection, client_address = sock.accept()              # accept
        data = connection.recv(structReceived.size)
        unpacked_data = structReceived.unpack(data)             # get unpacked data
        
    except Exception as e:
        print("Error connection: %s" % (e))
        
    if unpacked_data[0] == 0x01:                                # if get
        for i in range(2):
            opCode = 0x03                                       # opCode = data
            offset = blocNum * 512
            print offset
            data = content[offset : offset+512]                     # data = 512 bytes
            values = (opCode, blocNum, data)
            packed_data = structData.pack(*values)
            
            connection.sendall(packed_data)                         # send pycked_data
            blocNum += 1                                            # increment blockNum
            
            data = connection.recv(structReceived.size)
            unpacked_data = structAck.unpack(data)             # get unpacked data
            
            print str(unpacked_data[0]) + str(unpacked_data[1]) 