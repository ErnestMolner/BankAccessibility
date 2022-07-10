from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loginAndNavegateCredit import navegateAndLogCredit

def downloadTotals(key,dataFile):
    driver = navegateAndLogCredit(key,dataFile)
    driver.get("https://www.e-credit.ad/new/ca/group/andorra/consulta-moviments?maccId=1067874")
    delay = 15 #seconds of delay connsidered overtime
    #This waits are necessari because the web is slow and needs to load certain elements before its clickable
    #Clicking on the field to export files
    exportButton = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.ID,"boton_exportar")))
    exportButton.click()
    #Exporting csv file
    exportCSV = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME,"export_csv")))
    exportCSV.click()


#downloadTotals('/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/keys/credit.key','/media/sf_SharedFolder/bankFunctions/encryptionFunctionalties/encryptedData/creditEncryptedData.json')