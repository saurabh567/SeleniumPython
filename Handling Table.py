import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Edge(EdgeChromiumDriverManager().install())
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome(r"C:\Users\Get It Rent\Downloads\Software\chromedriver_win32")
driver.get("https://www.worldometers.info/coronavirus/")
driver.maximize_window()
time.sleep(10)
table_rows = driver.find_elements(By.XPATH, "//table[@id='main_table_countries_today']//tr[@class='odd']")
print("The number of rows in the table are:", len(table_rows))
# Finding the number of columns in table
table_columns = driver.find_elements(By.XPATH, "//table[@id='main_table_countries_today']//th")
print("The number of columns in the table are:", len(table_columns))
# Printing first columns values
table_first_column_values = driver.find_elements(By.XPATH, "//table[@id='main_table_countries_today']//td//a[@class]")
for value in table_first_column_values:
    print(value.text)

# Printing second columns values
table_second_column_values = driver.find_elements(By.XPATH, "//table[@id='main_table_countries_today']//td[9]")
for value in table_second_column_values:
    print(value.text)



#print("The number of first column values in the table are:", len(table_first_column_values))


