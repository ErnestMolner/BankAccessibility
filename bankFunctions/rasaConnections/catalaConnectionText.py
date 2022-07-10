import speech_recognition as sr
import requests
import json
import re
from makeTransfer import makeTransferFuncition
from downloadExpenses import downloadTotals
from termcolor import colored

def voiceConnection():
    r = sr.Recognizer()
    m = sr.Microphone()

    print("Un moment de silenci, si us plau...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Posta l'energia mínima d'activació {}".format(r.energy_threshold))
    print("Digues el vols fer ")
    with m as source: audio = r.listen(source)
    print("Missatge adquirit ara a processar...")
    try:
        # recognize speech using Google Speech Recognition
        value = r.recognize_google(audio, language="ca-ES")

        # we need some special handling here to correctly print unicode characters to standard output
        if str is bytes:  # this version of Python uses bytes for strings (Python 2)
            print("Tu as dit {}".format(value).encode("utf-8"))
            return(str("{}".format(value).encode("utf-8")))
        else:  # this version of Python uses unicode for strings (Python 3+)
            print(colored(str("Tu as dit {}".format(value)),'blue'))
            return(str("{}".format(value)))
    except sr.UnknownValueError:
        print("Oops! No he escoltat això")
        return("Retry")
    except sr.RequestError as e:
        print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
        return("Retry")

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
    txt = voiceConnection()
    if(txt != "Retry"):
        response = apiConnect(txt)
        #print(response)
        print(colored(response,'green'))
    else:
        response = "Retry"