#!/usr/bin/python

__author__ = 'Frederick NEY'

import sys
from Request import Request


def usage():
	print("-h or --help\n\tprint this usage")
	print("-H or --hostname\n\tserver full qualified domain name or ip address")
	print("-p or --port\n\tport number of the server")
	print("-m or --mode\n\tput or get")
	print("-la or --lose-average\n\taverage of packet lost over network")
	print("-i or --input\n\tinput file")
	print("-o or --output\n\toutput file")

	return


def main(argv):
	hostname = "localhost"
	port = 5000
	mode = "get"
	input_file = None
	output_file = None
	average = 0
	for n in range(len(argv)):
		if argv[n] == "-H" or argv[n] == "--hostname":
			hostname = argv[n + 1]
		if argv[n] == "-p" or argv[n] == "--port":
			port = int(argv[n + 1])
		if argv[n] == "-m" or argv[n] == "--mode":
			mode = argv[n + 1]
		if argv[n] == "-i" or argv[n] == "--input":
			input_file = argv[n + 1]
		if argv[n] == "-o" or argv[n] == "--output":
			output_file = argv[n + 1]
		if argv[n] == "--lose-average" or argv[n] == "-la":
			average = argv[n + 1]
		if argv[n] == "-h" or argv[n] == "--help":
			usage()
			sys.exit(0)
	if None == input_file:
		print("Missing input file")
		usage()
		sys.exit(-1)

	if None == output_file:
		output_file = input_file
	request = Request(hostname, port, average)
	request.request_connection(input_file, output_file, mode)
	return


if __name__ == '__main__':
	main(sys.argv)