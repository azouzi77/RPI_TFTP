import signal
import time
import random
 

   

    
class Timeout(Exception):
            pass
            
    
 
 
            def __init__(self, sec):
                        self.sec = sec
                        self.max_timer = random.randint(9, 16)  # Integer from 1 to 10, endpoints included
                        self.count=0
 
            def star_timer(self):
                        if count == max_timer:
                                    return -1;
                        else: 
                                    count = 1
                                    timer.start(3);
                                    return 0;
                                    print('timer_started')
        
            def restart_timer(self):
                        if count == maxtimer:
                                    return -1;
                        else:
                                    count= count+1;
                                    print('timer_restarted')
             
            def cancel_timer(self):
                        count == 0;
                        print('timer_canceled')
        
        
    
 
def main():
            try:
                        Timeout(3)
                        i = 0
                        while(1):
                             i = i + 1       
            except Exception:
                        print("exception")
            
            
            
            
            
            
            
if __name__=="__main__":
            main()

    
