# creating a hello world program
import time

import driver as driver
#print("hello world 1224")
#print("my name is saurabh")
#########################################
#a = 11.29
#b = 12.48
#c = a * b
#print(c)
###########################################

#num=0
#while(num<=10):
    #print(num)
    #num=num+1
###################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

webdriver.Chrome()
#webdriver.Firefox()
#webdriver.Edge()
#webdriver.Safari()

from selenium.webdriver.common.keys import Keys
#Import time
driver = webdriver.Chrome(r"C:\Users\Get It Rent\Downloads\Software\chromedriver_win32")
#driver.get("https://integration.shop.prodinger.de/customer/account/login/")
driver.maximize_window()
#time.sleep(10)
#Script for log in to the Prodinger Shop
# driver.find_element(By.XPATH, "//span[text()='Passwort anzeigen']").click()
# driver.find_element(By.XPATH, "//div[@class='control']//input[@id='email']").send_keys("kumar.saurabh@pixelmechanics.de")
# driver.find_element(By.XPATH, "//div[@class='control']//input[@title='Passwort']").send_keys("prodinger@1234")
# driver.find_element(By.XPATH, "//div[@class='primary']//button[@type='submit' ]//span[1]").click()
# time.sleep(10)

#Script for getting the Text
#ele=driver.find_element(By.XPATH, "//h3[contains(text(),'Sie haben')]").text
#print(ele)

#finding the total number of links in a page
#links=driver.find_elements(By.TAG_NAME, "a")
#print(len(links))

#Counting the number of header links(not working)
#ele1=driver.find_elements(By.XPATH("(//ul[@class='header links'])[1]"))
#print(ele1)

#Mouse Hover

# folien=driver.find_element(By.XPATH, "//nav[@class='navigation']//span[text()='Folien']")
# time.sleep(5)
# baufolien=driver.find_element(By.XPATH, "//nav[@class='navigation']//ul//li[@id='ui-id-6']//a//span")
# time.sleep(5)
# action=ActionChains(driver)
# action.move_to_element(folien).move_to_element(baufolien).click().perform()


#makemytrip website
driver.get("https://www.makemytrip.com/")
#time.sleep(3)
driver.find_element(By.XPATH, "//li[@data-cy='roundTrip']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//div[@class='fsw_inputBox searchCity inactiveWidget ']").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//div[@id='react-autowhatever-1']//div[@class='calc60']//p[text()='Bangkok, Thailand']").click()
# time.sleep(5)
# select = Select(dropdown_element)
# select.select_by_visible_text("Bangkok, Thailand")

#driver.find_element(By.XPATH, "//div[@class='fsw_inputBox searchToCity inactiveWidget '] ").click()
#time.sleep(5)
#driver.find_element(By.XPATH, "(//p[contains(text(),'Goa - Dabolim Airport, India')])[2]").click()

#Handling calenders
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[contains(.,'Departure')]").click()













#time.sleep(5)

