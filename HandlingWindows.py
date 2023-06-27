import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#To print title of all windows in the current session

driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[text()='Services']").click()
print(driver.current_window_handle)#Returning the id of the parent window
time.sleep(5)
handles=driver.window_handles
size=len(handles)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

#to close the parent window
if driver.title=="Jobs - Recruitment - Job Search - Employment - Job Vacancies - Naukri.com":
    driver.close()

time.sleep(5)
driver.quit()






