from emailFunctionalties.extractimap import dayImapExtraction
import time
import json 
import re


def getConfirmationCode(data):
    
    #This delay is set to make the program wait so that the phone has time to send the email. 
    time.sleep(30)
    emailList = {} #Iniciate the variable as a json
    #we use the email funciotnalty to obtain the email list as a json
    data = dayImapExtraction(data["email"],data["emailpass"])
    emailList = json.loads(data) #It reparces the data as json

    #making the conversion to string type
    totalEmailNum = int(emailList["mailNum"])
    #mail Num retruns the number of emails the index starts at zero so we need to subtract one to obtane the last position
    totalEmailNum = totalEmailNum - 1

    creditExtractionRegex = re.compile(r'(?<=Use the code )\d+') #This is the pattern that represents that will allow us to extrat the text message code value

    matchingValue = creditExtractionRegex.search(emailList['subjectIndex' + str(totalEmailNum)]) #this refeairs to the las mail message recived
    #This returns the regex match for the code number
    return matchingValue.group()
    

def getConfirmationCodeTrasfer(data):
    
    #This delay is set to make the program wait so that the phone has time to send the email. 
    time.sleep(30)
    emailList = {} #Iniciate the variable as a json
    #we use the email funciotnalty to obtain the email list as a json
    data = dayImapExtraction(data["email"],data["emailpass"])
    emailList = json.loads(data) #It reparces the data as json

    #making the conversion to string type
    totalEmailNum = int(emailList["mailNum"])
    #mail Num retruns the number of emails the index starts at zero so we need to subtract one to obtane the last position
    totalEmailNum = totalEmailNum - 1

    creditExtractionRegex = re.compile(r'(?<=Utilitzeu_el_codi_)\d+') #This is the pattern that represents that will allow us to extrat the text message code value

    matchingValue = creditExtractionRegex.search(emailList['subjectIndex' + str(totalEmailNum)]) #this refeairs to the las mail message recived
    #This returns the regex match for the code number
    return matchingValue.group()