#

class Put:
    
    socket = None
    
    def __init__(self, socket):
        self.socket = socket
        
        
    def send_ack(self, blocNum):                                 # send ACK:
        opCode = 0x04                                           # opcode = ACK
        values = (opCode, blocNum)
        packed_data = structAck.pack(*values)                   # pack struct
        self.socket.sendall(packed_data)                        # send ACK
        
        
    def send_content(self, blocNum, data):                          # send Data:
        opCode = 0x03                                           # opCode = data
        values = (opCode, blocNum, data)
        packed_data = structAck.pack(*values)                   # pack struct
        self.socket.sendall(packed_data)                        # send data
        
        
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
