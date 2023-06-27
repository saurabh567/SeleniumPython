import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://artoftesting.com/sampleSiteForSelenium")
# source = driver.find_element(By.XPATH, "//img[@alt='art of testing']")
# target = driver.find_element(By.XPATH, "//div[@id='targetDiv']")
# action=ActionChains(driver)
# action.drag_and_drop(source, target).perform()
# time.sleep(5)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-1.html")
source = driver.find_element(By.XPATH, "//div[@id='box2']")
target = driver.find_element(By.XPATH, "//div[@id='dropBox']")
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()
time.sleep(5)
