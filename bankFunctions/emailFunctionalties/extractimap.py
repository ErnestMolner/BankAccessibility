import imaplib
import email
import time
import json

def dayImapExtraction(email_user,email_pass):
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    mail.login(email_user, email_pass)
    mail.select()

    loopcontrol = 0 # This loop control is created to iniciate the loop turn
    dataJson = {} # This iniciates our json transfer object with our filterd mails

    type, data = mail.search(None, "(ON {0})".format( time.strftime("%d-%b-%Y") ) ) #This filter is aplayed to only retrun mail recived in the last 24h
    mail_ids = data[0].decode('utf-8')
    id_list = mail_ids.split()
    mail.select('INBOX', readonly=True)
    for i in id_list:
        typ, msg_data = mail.fetch(str(i), '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                #Email respone print examples

                #print(msg['from']+"\t"+msg['subject'] + " " + msg['Date'])
                #print(msg['subject'] + " " + msg['Date'])
                #print(msg)

                #Email respone print examples
                
                dataJson["subjectIndex" + str(loopcontrol)] = msg['subject'] #we dynamicaly add the subject to the json file
                loopcontrol = loopcontrol + 1
    dataJson["mailNum"] = loopcontrol
    json_data = json.dumps(dataJson)
    #print(json_data)
    return json_data
