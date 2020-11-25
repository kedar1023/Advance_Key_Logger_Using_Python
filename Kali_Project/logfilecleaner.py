
import re

def clean():

    with open('logfile.txt','r') as file:

        msg = file.read()


    msg = msg.replace(' ', '') #Remove spaces
    msg = re.sub(re.compile(r"<Key.space:''>"), ' ', msg)  #Replace in space by ''
    regex_key = re.compile(r'(<Key\..*?)(?:\'| |\d|\"|Key.esc|\s)>(>?)') #Collect all special char/keys

    msg = re.sub(regex_key, '', msg) #Empty char with string
    msg = msg.replace('\'', '') #Quote with empty string
    msg = msg.replace(',', '') #Comma with empty string

    print(msg)    


clean()