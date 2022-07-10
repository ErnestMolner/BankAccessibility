from crypt import methods

#from requests import request
from flask import Flask, request, render_template
import json
from encryptionKeyGeneration import generateKey
from encryptFileUsingKey import encryptFile
from downloadExpenses import downloadTotals
from makeTransfer import makeTransferFuncition

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkTotalsFont')
def front():
    return render_template('checkTotals.html')

@app.route('/addBankInfoAndEncryp', methods=['POST'])
def add_BankInfo():
    #We get the request
    info = request.get_json()
    #We obtain the to be file name 
    fileName = info['fileName']
    #We obtain the key name 
    keyName = info['key']
    #We obtain the user name
    userName = info['user']
    #We obtain the user pow
    passWord = info['pass']
    #We obtain the user eamil
    email = info['email']
    #We obtain the email pow
    emailPow = info['emailpass']
    #Parsing the message into a unified payload
    filePayLoad = {
        "user":userName,
        "pass":passWord,
        "email":email,
        "emailpass":emailPow
    }
    #Write our temporal file
    jsonData = json.dumps(filePayLoad)
    f = open(f"/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/unEncryptedData/{fileName}.json", "w")
    f.write(jsonData)
    f.close()
    #KeyGeneration 
    generateKey(f"/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/{keyName}.key")

    #DataEncription using generated key
    encryptFile(f"/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/{keyName}.key",f"/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/unEncryptedData/{fileName}.json",f"/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/{fileName}.json")

    print(jsonData)
    return f'DataRecived Key {keyName} ' + f'File Name {fileName}'

@app.route('/checkTotals', methods=['POST'])
def checkTotals():
    #Getting the request info in the json
    info = request.get_json()
    #We obtain the name of key to be used and the file data.
    keyName = info['key']
    fileName = info['fileName']
    downloadTotals(f'/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/{keyName}.key',f'/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/{fileName}.json')

    return 'check Done'

@app.route('/makeTransfer', methods=['POST'])
def makeTransaction():
    #Getting the request info in the json
    info = request.get_json()
    print(info)
    #We obtain the name of key to be used and the file data.
    keyName = info['key']
    fileName = info['fileName']
    importMoney = info['import']
    makeTransferFuncition(f'/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/{keyName}.key',f'/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/{fileName}.json','AD8500010000416292400100','BotTransactionTest',importMoney,'Ernest Molner Marti')
    return 'Trasfer Made'