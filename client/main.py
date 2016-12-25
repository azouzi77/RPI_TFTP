#!/usr/bin/python
__author__ = 'Frederick NEY'

import sys
from client import Request as App


def usage():
	return


def main(argv):
	hostname = "localhost"
	port = 5000
	mode = "get"
	input_file = None
	output_file = None
	average = 0
	for n in range(len(argv)):
		if argv[n] == "--H" or argv[n] == "--hostname":
			hostname = argv[n + 1]
		if argv[n] == "--p" or argv[n] == "-port":
			port = int(argv[n + 1])
		if argv[n] == "--m" or argv[n] == "-mode":
			mode = argv[n + 1]
		if argv[n] == "--i" or argv[n] == "-input":
			input_file = argv[n + 1]
		if argv[n] == "--o" or argv[n] == "-output":
			output_file = argv[n + 1]
		if argv[n] == "--lose_average" or argv[n] == "-la":
			average = argv[n + 1]
		if argv[n] == "--h" or argv[n] == "-help":
			usage()
	if None == input_file:
		print("Missing input file\n")
	if None == output_file:
		output_file = input_file
	request = App.Request(hostname, port, average)
	request.request_connection(input_file, output_file, mode, average)
	return


if __name__ == '__main__':
	main(sys.argv)