#import os to remove file when encrypted file has been created 

import os

#import the- required module
from cryptography.fernet import Fernet

#importing colorama for error message
import colorama
from colorama import Fore


def encryptFile(keyfile, originalFile, encryptedFile):
     #open the key
     with open(keyfile, 'rb') as unlock:
          key = unlock.read()

     #use the generated key
     f = Fernet(key)

     #open the original file to encrypt
     with open(originalFile, 'rb') as original_file:
          original = original_file.read()

     #encrypt the file
     encrypted = f.encrypt(original)
     #you can write the encrypted data  file into a enc_sample.txt
     with open (encryptedFile, 'wb') as encrypted_file:
          encrypted_file.write(encrypted)
     #note you can delete your original file if you wantls
     
     if os.path.exists(originalFile):
          os.remove(originalFile)
          print(Fore.GREEN + "File succesfully encrypted")
     else:
          #This can be a serious issue so ill print it in red 
          print(Fore.RED + "Error deliting unencrpyted file delete manualy !!!!!")