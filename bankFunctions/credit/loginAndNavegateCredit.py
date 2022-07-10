from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
from encryptionFunctionalties.readEncryptedFileModulus import decryptJson
#from coordenatesFlow import coordenatesFlow
from confirmatonCodeCredit import getConfirmationCode

def navegateAndLogCredit(key,dataFile):
    data = decryptJson(key,dataFile) #decrypting the data file
    driver = webdriver.Firefox()
    #Navegate to the main credit page
    driver.get("https://comercial.creditandorragroup.ad/en/e-credit")

    #Find the e-credit button and click it
    driver.find_element(By.XPATH,"/html/body/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/ul/li[2]/a").click()

    #Fill the user field
    userField = driver.find_element(By.ID,"unid")
    userField.clear()
    userField.send_keys(data["user"])

    #Fill the pow field
    powField = driver.find_element(By.ID,"psxid")
    powField.clear()
    powField.send_keys(data["pass"])
    powField.send_keys(Keys.ENTER)
    #This flow calls on the filling of the coordenates card
    #coordenatesFlow(driver,key,dataFile) Sadly this method is deprecated 

    #Check if the confirmation code page appears
    delay = 13 #seconds of delay connsidered overtime
    confirmationPageExist = True

    #This try catch is done because the page reloades and therefore we need to wait for it to be ready
    try:
        confirmationField = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,"password")))

        
    except TimeoutException:
        #If the element dosen't exist we will consider that no cordenate page exists
        confirmationPageExist = False
        print("Load time test exeded considering sms confirmation page did not appear at login")
    
    if(confirmationPageExist):
        #Invoking the flow that returns us the confirmation code
        confirationCode = getConfirmationCode(data)
    
        #Fill confirmation code
    
        confirmationField.clear()
        confirmationField.send_keys(confirationCode)
        confirmationField.send_keys(Keys.ENTER)
    



    return driver

#navegateAndLogCredit('/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/credit.key','/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/creditEncryptedData.json')