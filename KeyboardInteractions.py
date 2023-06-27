import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
driver.maximize_window()
search_element=driver.find_element(By.XPATH, "//input[@type='text']")
search_element.send_keys("best gift for wife anniversary special")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(4)