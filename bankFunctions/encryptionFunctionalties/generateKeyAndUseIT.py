from encryptionKeyGeneration import generateKey
from encryptFileUsingKey import encryptFile
#This file allowyou to generate keys as a test and use them
#We generate the key we are going to use to encrypt our credential json
#generateKey('keys/andBank.key')
generateKey('keys/credit.key')
#We destroy our data jason and store the encrypted file
#encryptFile('keys/andBank.key','unEncryptedData/andBankData.json','encryptedData/andBankEncryptedData.json')
encryptFile('keys/credit.key','unEncryptedData/creditData.json','encryptedData/creditEncryptedData.json')
#testd = decryptJson('test.key','testEncrypted.json')
#print (testd)