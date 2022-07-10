import requests
import json
import re
from makeTransfer import makeTransferFuncition
from downloadExpenses import downloadTotals

def apiConnect(message):
    API_ENDPOINT = "http://localhost:5005/webhooks/rest/webhook"

    messagePayload = {
        "sender": 'default',
        "message": message
      }

    jsonData = json.dumps(messagePayload)

    r = requests.post(url = API_ENDPOINT, data = jsonData)
    #Expression to extract the response text from api response
    regexTextExtraction = re.compile(r'(?<=\"text\":\").*(?=\"}\])')
    matchingValue = regexTextExtraction.search(r.text)
    recivedText = matchingValue.group()
    return (recivedText)

response = ""
firstMessage = True
#Expression to extract confirmation message
confirmationMessageRegex = re.compile(r'Entesos, proseguim amb la transferencia de ')
checkMakeTransfer = False
#Expression to extract the confirmation value
confirmationMessagValue = re.compile(r'[\d\.]+(?= EURO)')

while(response != "adeu"):
    if(firstMessage):
        #Start message
        print("Disposes de dues opcions \nRealitzar transferència\nConsulta de càrrecs")
        firstMessage = False
    else:
        #Checking for confirmation message
        checkMakeTransfer = bool(confirmationMessageRegex.search(response))
    #If confirmation value recived extract that value
    if(checkMakeTransfer):
        transferValue = confirmationMessagValue.search(response)
        recivedValue = transferValue.group()
        makeTransferFuncition('/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/credit.key','/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/creditEncryptedData.json','AD8500010000416292400100','BotTransactionTest',recivedValue,'Ernest Molner Marti')
    
    #Encendre el flow de descarregar totals es detecta l'intencio
    if(response == "Comprovant costos"):
        downloadTotals('/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/credit.key','/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/creditEncryptedData.json')
    #Preguntes i respostes amb el systema inteligent
    txt = input("Digues el vols fer: ")
    response = apiConnect(txt)
    print(response)