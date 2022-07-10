#import the- required module
from curses import keyname
from cryptography.fernet import Fernet

def generateKey(keyname):
     #generate the key
     key = Fernet.generate_key()
     #string the key into a file
     with open(keyname, 'wb') as unlock:
          unlock.write(key)

