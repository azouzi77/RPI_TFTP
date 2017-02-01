#!/usr/bin/python

__author__ = 'Frederick NEY and Stephane OVERLEN'

import sys
import socket
import Resources
from Core import *
from Get import *
from Timeout import *

def usage():
	print("-h or --help\n\tprint this usage")
	print("-p or --port\n\tport number of the server")
	print("-la or --lose-average\n\taverage of packet lost over network")
	print("-f or --folder\n\tfolder where tftp server will run")
	return


def main(argv):
	port = 5000
	folder = None
	packet_loss = 0

	for n in range(len(argv)):
		if argv[n] == "-p" or argv[n] == "--port":
			port = int(argv[n + 1])
		if argv[n] == "-h" or argv[n] == "--help":
			usage()
			sys.exit(0)
		if argv[n] == "-la" or argv[n] == "--lose-average":
			if int(argv[n + 1]) < 0:
				packet_loss = 0
			elif int(argv[n + 1]) >= 100:
				packet_loss = 100
			else:
				packet_loss = int(argv[n + 1])
		if argv[n] == "-f" or argv[n] == "--folder":
			folder = argv[n + 1]
	if None == folder:
		print("No such folder.")
		usage()
		sys.exit(-1)
	socket_srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	socket_srv.bind(("0.0.0.0", port))
	data, addr = socket_srv.recvfrom(PACKET_SIZE)
	timer = Timeout(15.0, socket_srv)
	while True:
		if None == data and None == addr:
			timer.cancel_timer()
			data, addr = socket_srv.recvfrom(PACKET_SIZE)
		app = Core(socket_srv, data, addr, packet_loss, folder)
		data, addr = app.GetAnswer()
	return


if __name__ == '__main__':
	main(sys.argv)
