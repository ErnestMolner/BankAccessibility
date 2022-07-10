from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
from encryptionFunctionalties.readEncryptedFileModulus import decryptJson
from confirmatonCode import getConfirmationCode



    

def navegateAndLoginAndBank(key,dataFile):

    data = decryptJson(key,dataFile) #decrypting the data file
    #print(data)
    driver = webdriver.Firefox()
    #Navegate to the andBank login page
    driver.get("https://homebanking.andbank.com")
    delay = 13 #seconds of delay connsidered overtime for web connection
    #Fill the user field
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID,"user")))
    userField = driver.find_element(By.ID,"user")
    userField.clear()
    userField.send_keys(data["user"])

    #Fill the pow field
    powField = driver.find_element(By.ID,"password")
    powField.clear()
    powField.send_keys(data["pass"])
    powField.send_keys(Keys.ENTER)

    #Invoking the flow that returns us the confirmation code
    confirationCode = getConfirmationCode(data)

    #Fill confirmation code
    confirmationField = driver.find_element(By.ID,"coordinateAnswerId")
    confirmationField.clear()
    confirmationField.send_keys(confirationCode)
    confirmationField.send_keys(Keys.ENTER)

navegateAndLoginAndBank('/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/andBank.key','/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/andBankEncryptedData.json')

