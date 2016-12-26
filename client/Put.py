#
import client.Utils
import client.Resources


class Put:
    
    socket = None
    
    def __init__(self, socket):
        self.socket = socket

    def send_ack(self, blocNum):                                # send ACK:
        opCode = client.Resources.ACK                                           # opcode = ACK
        struct = client.Utils.Structure(opCode)               # pack struct
        ack_struct = struct.ack_struct(blocNum)
        self.socket.sendall(ack_struct)                        # send ACK

    def send_content(self, blocNum, data):                      # send Data:
        opCode = client.Resources.DATA                                           # opCode = data
        struct = client.Utils.Structure(opCode)
        data_struct = struct.data_struct(blocNum, data)         # pack struct
        self.socket.sendall(data_struct)                        # send data
        
        
"""
    def reqSend(sock, req, fileName, loss):                     # send request
        if req == 'get':                                        # set opCode
            opCode = 0x01
            
            values = (opCode, fileName, 0, 'octet', 0)
            packed_data = structSend.pack(*values)              # pack struct
            sock.sendall(packed_data)                           # send request
            
            data = sock.recv(structData.size)
            unpacked_data = structData.unpack(data)             # get unpacked data
            
            return unpacked_data
            
        elif req == 'put':
            opCode = 0x02
"""
