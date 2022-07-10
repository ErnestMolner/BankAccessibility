#import the json parser
import json

#import the- required module
from cryptography.fernet import Fernet

def decryptJson(keyFile, encryptedJson):

     #open the key
     with open(keyFile, 'rb') as unlock:
          key = unlock.read()

     #first use the key
     f = Fernet(key)
     #open the encrypted file
     with open(encryptedJson, 'rb') as encrypted_file:
          encrypted = encrypted_file.read()
     #decrypt the file
     decrypted = f.decrypt(encrypted)

     #Json parse the file 

     return json.loads(decrypted)