import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)
#1)MOUSEHOVER
driver.get("https://www.amazon.in/")
driver.maximize_window()
#object of ActionChains
action=ActionChains(driver)
#identify element
m=driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']")
#hover over element
action.move_to_element(m).perform()

#2)CLICK
action.click(driver.find_element(By.XPATH, "//div[@id='nav-cart-count-container']")).perform()
#3)DOUBLE CLICK
driver.get("https://artoftesting.com/sampleSiteForSelenium")
time.sleep(10)
#action.double_click(driver.find_element(By.XPATH,"//button[@id='dblClkBtn']")).perform()










