#
"""
        values = (nodePort, msg)
        packer = struct.Struct('I s')
        packed_data = packer.pack(*values)
        
        sock.sendall(packed_data)                               # send message
        sock.close()                                            # close socket

        unpacker = struct.Struct('I s')
        data = self.clientsocket.recv(unpacker.size)
        unpacked_data = unpacker.unpack(data)               # get unpacked data
        self.clientsocket.close()
"""


"""
apt-get tftpd

Client TFTP


doctest pour inclure les tests unitaires


"""
import binascii
import socket
import struct
import sys

structSend = struct.Struct('!h 7s h 5s h')
structData = struct.Struct('!h h 512s')
structAck = struct.Struct('!h h')
blocNum = 0

def dataGet(sock):
    data = sock.recv(structData.size)
    unpacked_data = structData.unpack(data)                 # get unpacked data

    for receivedData in unpacked_data:
        print str(receivedData) + ' ' + str(len(str(receivedData)))


def dataSend(sock, blocNum, dataType):
    if dataType == 'ACK':
        opCode = 0x04                                           # opcode = ACK
        values = (opCode, blocNum)
        packed_data = structAck.pack(*values)                   # pack struct
        sock.sendall(packed_data)                               # send ACK
    

def reqSend(sock, req, fileName, loss):
    if req == 'get':                                        # set opCode
        opCode = 0x01
        
        values = (opCode, fileName, 0, 'octet', 0)
        packed_data = structSend.pack(*values)                  # pack struct

        for sentData in values:
            print 'sending ' + str(sentData)
            
        sock.sendall(packed_data)                               # send request
        
        data = sock.recv(structData.size)
        unpacked_data = structData.unpack(data)                 # get unpacked data
        
        return unpacked_data
        
    elif req == 'put':
        opCode = 0x02
        
        
    


def connect(dns, port):                                     # create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (dns, port)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    
    return sock


func = ""
#    var = raw_input(">> ")                                              # get user input

################################# HARD CODING ######################################
func = 'mytftpc'
req = 'get'
dns = 'localhost'
port = 10000
fileName = 'test100'
loss = 0
################################# HARD CODING ######################################

#    func, req, dns, port, fileName, loss = var.split(" ", 5)

print func + ' ' + req + ' ' + dns + ' ' + str(port) + ' ' + fileName + ' ' + str(loss)

while func != 'mytftpc':
    print 'usage: mytftpc <put/get> <nom_DNS_du_serveur> <numero_de_port> <nom_fichier> <taux_de_perte>'

while req != 'put' and req != 'get':
    print 'usage: mytftpc <put|get> <nom_DNS_du_serveur> <numero_de_port> <nom_fichier> <taux_de_perte>'

sock = connect(dns, port)
data = reqSend(sock, req, fileName, loss)     # send requet & get server datas
dataSend(sock, blocNum, 'ACK')

while(len(data[2]) == 512):
    if data[0] == 0x03:
        dataGet(sock)
        dataSend(sock, blocNum, data[0])
        
print >>sys.stderr, 'closing socket'
sock.close()
