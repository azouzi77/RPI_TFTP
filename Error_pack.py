class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """


    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg



class TransitionError(Error):

    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """


    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
        
    def SendError():
    
    
    def IsCritical():
    
    
    def PrintError():
    
    

if          error 0x00 IsCritical()
else        error 0x01 IsCritical()
else        error 0x02 IsCritical() 
else        error 0x03 IsCritical()
else        error 0x04 Senderror()
else        error 0x05 IsCritical()
else        error 0x06 IsCritical()

#---------------------------------------------------------------


class TftpPacketERR(TftpPacket):
    """
::

            2 bytes  2 bytes        string    1 byte
            ----------------------------------------
    ERROR | 05    |  ErrorCode |   ErrMsg   |   0  |
            ----------------------------------------

    Error Codes

    Value     Meaning

    0         Not defined, see error message (if any).
    1         File not found.
    2         Access violation.
    3         Disk full or allocation exceeded.
    4         Illegal TFTP operation.
    5         Unknown transfer ID.
    6         File already exists.
    7         No such user.
    8         Failed to negotiate options
    """
    def __init__(self):
        TftpPacket.__init__(self)
        self.opcode = 5
        self.errorcode = 0
        # FIXME: We don't encode the errmsg...
        self.errmsg = None
        # FIXME - integrate in TftpErrors references?
        self.errmsgs = {
            1: "File not found",
            2: "Access violation",
            3: "Disk full or allocation exceeded",
            4: "Illegal TFTP operation",
            5: "Unknown transfer ID",
            6: "File already exists",
            7: "No such user",
            8: "Failed to negotiate options"
            }

    def __str__(self):
        s = 'ERR packet: errorcode = %d' % self.errorcode
        s += '\n    msg = %s' % self.errmsgs.get(self.errorcode, '')
        return s

    def encode(self):
        """Encode the DAT packet based on instance variables, populating
        self.buffer, returning self."""
        format = "!HH%dsx" % len(self.errmsgs[self.errorcode])
        log.debug("encoding ERR packet with format %s", format)
        self.buffer = struct.pack(format,
                                  self.opcode,
                                  self.errorcode,
                                  self.errmsgs[self.errorcode])
        return self

    def decode(self):
        "Decode self.buffer, populating instance variables and return self."
        buflen = len(self.buffer)
        tftpassert(buflen >= 4, "malformed ERR packet, too short")
        log.debug("Decoding ERR packet, length %s bytes", buflen)
        if buflen == 4:
            log.debug("Allowing this affront to the RFC of a 4-byte packet")
            format = "!HH"
            log.debug("Decoding ERR packet with format: %s", format)
            self.opcode, self.errorcode = struct.unpack(format,
                                                        self.buffer)
        else:
            log.debug("Good ERR packet > 4 bytes")
            format = "!HH%dsx" % (len(self.buffer) - 5)
            log.debug("Decoding ERR packet with format: %s", format)
            self.opcode, self.errorcode, self.errmsg = struct.unpack(format,
                                                                     self.buffer)
        log.error("ERR packet - errorcode: %d, message: %s"
                     % (self.errorcode, self.errmsg))
        return self


#--------------------------------------------------------------------------



class TftpErrors(object):
    """This class is a convenience for defining the common tftp error codes,
    and making them more readable in the code."""
    NotDefined = 0
    FileNotFound = 1
    AccessViolation = 2
    DiskFull = 3
    IllegalTftpOp = 4
    UnknownTID = 5
    FileAlreadyExists = 6
    NoSuchUser = 7
    FailedNegotiation = 8

class TftpException(Exception):
    """This class is the parent class of all exceptions regarding the handling
    of the TFTP protocol."""
    pass

class TftpTimeout(TftpException):
    """This class represents a timeout error waiting for a response from the
    other end."""
    pass

#----------------------------------------------------------------------------






  # Handle errors
                except Exception as err:
                    message = "Packetnr: {0}, retry count: {1}, header: {2}, error: {3}\ntraceback: {4}"
                    self.log("write exception", params=(remote, local, mode), msg=message.format(packetnr, retry_count, rcv_buffer[:4], err,  traceback.format_exc()))

                    # Handle timeouts
                    if self.TIME_OUT in err.args:
                        timeout = True
                        retry_count += 1

                        if retry_count >= self.MAX_RETRY_COUNT:
                            print("Max retried sends... leaving")
                            break
                        else:
                            self.log("writetimeout exception", params=(remote, local, mode), msg=message.format(packetnr, retry_count, rcv_buffer[:4], err,  traceback.format_exc()))

            success = True
            self.log("write success", params=(remote, local, mode), msg = "Success in writing file {0} to host {1}, total bytes sent: {2}, total retry counts: {3}, execution time: {4} seconds".format(remote, self.addr, len(file_buffer), retry_count, time.time() - start_time))
            

        # Handle TFTP specific errors
        except TFTPException as terr:
            self.log("write: tftpexception", params=(remote, local, mode), msg="Error: {0}, traceback: {1}".format(err, traceback.format_exc()))

        # Handle all other errors        
        except Exception as err:
            self.log("write: outerexception", params=(remote, local, mode), msg="Error: {0}, traceback: {1}".format(err, traceback.format_exc()))

        # Close resources
        finally:
            if file:
                file.close()

        return success
    
 
