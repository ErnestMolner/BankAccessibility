from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore
from encryptionFunctionalties.readEncryptedFileModulus import decryptJson

def coordenatesFlow(driver,key,dataFile):
    data = decryptJson(key,dataFile)
    delay = 13 #seconds of delay connsidered overtime
    #We will always asume that the coordenate page exists
    coordenatesPageExist = True

    #This try catch is done because the page reloades and therefore we need to wait for it to be ready
    try:
        coordenatesNum = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/div/div/div/div/div/form/section/div/div[2]/div[2]/div/div/p")))
        coordenatesNum = coordenatesNum.get_attribute('innerHTML')
        coordenatesValue = data[coordenatesNum]
        #We only need the inner html number we dont need the browser element
        print(coordenatesNum)
        print(coordenatesValue)
        
    except TimeoutException:
        #If the element dosen't exist we will consider that no cordenate page exists
        coordenatesPageExist = False
        print("Load time test exeded considering coordenate page did not appear at login")

    if(coordenatesPageExist):
        try:
            button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/div/div/div/form/section/div/div[2]/div[2]/div/div/ul/li[1]/button')))
            #If the first button has loaded all the other have loaded too
            button_dictionary = {} #dictionary of buttons
            #Range of button numbers in credit cordenates, there is 10 numberes ranging from 1 to 10
            for x in range(1,11):
                serchString = '/html/body/div/div/div/div/div/div/div/div/form/section/div/div[2]/div[2]/div/div/ul/li[{}]/button'.format(x)
                button = driver.find_element(By.XPATH, serchString)
                print("button{} ".format(x) + button.get_attribute('innerHTML'))
                # create the dicctionary with the inner html value as key and the button as the item
                button_dictionary[button.get_attribute('innerHTML')] = button
        except TimeoutException:
            print(Fore.RED + "Error page num elements not loaded in time")

        #We iterate all characters of the code and press the corresponding numberes
        for i in range(len(coordenatesValue)):
            button_dictionary[coordenatesValue[i]].click()
    
        #Click the submit button
        #driver.find_element(By.ID,"btnSiguiente").click()

    #driver.quit()