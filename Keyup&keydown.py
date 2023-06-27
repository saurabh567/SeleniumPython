import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
driver.maximize_window()
header_links = driver.find_elements(By.XPATH,"//div[@id='nav-xshop-container']//a")

for header_link in header_links:
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(header_link).key_up(Keys.CONTROL).perform()
time.sleep(15)


#key_up--is used to release the particular key