

from time import sleep
from threading import Timer


class Flag ():
    flag = 1
alpha = Flag()

def stop_timer():
            #flag a zero
            alpha.flag = 0
            
            
def cancel_timer():
            #flag a un
            alpha.flag = 1



def start_timer():
            print("Timeout!")# After X seconds, "Timeout!" will be printed



t = Timer(7.0, start_timer)
t.start()              # After 7 seconds, "Timeout!" will be printed if no event
stop_timer()            #event1
cancel_timer()          #event2


sleep(5.0)


flag = alpha.flag
if flag==1:     # wait event
     t.cancel()        
     print('timer_canceled') #if flag 1
if flag==0:
            t.cancel()
            print('timer_stop') #if flag 0
            
            
 #exception pour lever timer
 
"""
def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    import signal

    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError()

    # set the timeout handler
    signal.signal(signal.SIGALRM, handler) 
    signal.alarm(timeout_duration)
    try:
        result = func(*args, **kwargs)
    except TimeoutError as exc:
        result = default
    finally:
        signal.alarm(0)

    return result




class watchdog():
  def _timeout(self):
    #raise self
    raise TypeError

  def __init__(self):
    self.t = Timer(1, self._timeout)

  def start(self):
    self.t.start()

try:
  w = watchdog()
  w.start()
  sleep(2)
except TypeError, e:
  print "Exception caught"
else:
  print "Of course I didn't catch the exception"
  """          

     
     
 
