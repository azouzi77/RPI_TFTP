#
import Utils
import Resources


class Put:
    
    socket = None
    
    def __init__(self, socket, address, port):
        self.socket = socket
        self.address = address
        self.port = port

    def send_ack(self, blocNum):                                # send ACK:
        opCode = Resources.ACK                                           # opcode = ACK
        struct = Utils.Structure(opCode)               # pack struct
        ack_struct = struct.ack_struct(blocNum)
        self.socket.sendto(ack_struct, (self.address, self.port))                        # send ACK

    def send_content(self, blocNum, data):                      # send Data:
        opCode = Resources.DATA                                           # opCode = data
        struct = Utils.Structure(opCode)
        data_struct = struct.data_struct(blocNum, data)         # pack struct
        self.socket.sendto(data_struct, (self.address, self.port))                        # send data
        
        
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
