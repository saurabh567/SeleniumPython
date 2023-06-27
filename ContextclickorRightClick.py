import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
source=driver.find_element(By.XPATH, "//a[.='Amazon Pay']")
action = ActionChains(driver)
action.context_click(source).perform()
action.release()
time.sleep(3)