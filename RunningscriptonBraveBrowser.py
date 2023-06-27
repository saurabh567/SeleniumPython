import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
driver.implicitly_wait(10)
driver.get("https://integration.shop.prodinger.de/customer/account/login/")
driver.find_element(By.XPATH, "//button[@type='submit']").click()