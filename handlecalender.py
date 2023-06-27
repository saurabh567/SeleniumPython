import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

1
driver.get("https://www.redbus.in/")
time.sleep(5)
driver.find_element(By.XPATH, "//span[@class='fl icon-calendar_icon-new icon-onward-calendar icon']").click()
time.sleep(10)
#driver.find_element(By.XPATH, "//table[@class='rb-monthTable first last']//tr//td[@class='current day']").click()
driver.find_element(By.XPATH, "//table[@class='rb-monthTable first last']//tr[4]//td[4]").click()

"""(multiline comment ,for that give continous 3 doble qutes)
this is a pycharm
pycharm is cool

"""