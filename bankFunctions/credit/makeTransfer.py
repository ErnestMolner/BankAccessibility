from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loginAndNavegateCredit import navegateAndLogCredit
from encryptionFunctionalties.readEncryptedFileModulus import decryptJson
from confirmatonCodeCredit import getConfirmationCodeTrasfer


def makeTransferFuncition(key,dataFile,acountNum,concept,quantityToTransfer,nameOfPerson):
    driver = navegateAndLogCredit(key,dataFile)
    driver.get("https://www.e-credit.ad/new/ca/group/andorra/nova-transferencia")
    delay = 15 #seconds of delay connsidered overtime
    #This waits are necessari because the web is slow and needs to load certain elements before its clickable
    #Clicking on the field Un altre compte de credit andorra o entitat
    acountELement = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div[3]/div[1]/div/div/div/div/div/section/div/form/div[3]/div[2]/div[1]/div[5]/div/label/span")))
    acountELement.click()
    #Obtainig the element where you can fill IBAN number
    ibanField = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID,"IBANDestino")))
    ibanField.clear()
    ibanField.send_keys(acountNum)
    #Filling the name of the person thats to recive the transaction
    recipient = driver.find_element(By.ID,"beneficiario")
    recipient.clear()
    recipient.send_keys(nameOfPerson)
    #Filling the transaction concept
    trasactionConcept = driver.find_element(By.ID,"concepto")
    trasactionConcept.clear()
    trasactionConcept.send_keys(concept)
    #Filling the amount to transfer
    transactionImport = driver.find_element(By.ID,"importe")
    transactionImport.clear()
    transactionImport.send_keys(quantityToTransfer)
    #Click Continue with transaction
    driver.find_element(By.ID,"siguiente").click()
    #Extracting the email with the confirmation code
    data = decryptJson(key,dataFile) #decrypting the data file
    confirmationCode = getConfirmationCodeTrasfer(data)
    #Filling The confirmation code
    confirmationCodeFiled = driver.find_element(By.ID,"password")
    confirmationCodeFiled.clear()
    confirmationCodeFiled.send_keys(confirmationCode)
    #Confirm The transaction
    #driver.find_element(By.ID,"confirmar").click()




#makeTransferFuncition('/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/credit.key','/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/creditEncryptedData.json','AD8500010000416292400100','BotTransactionTest','100','Ernest Molner Marti')