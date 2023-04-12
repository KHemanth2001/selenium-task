from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service_log_path="D:/selenium/chromedriver.exe")
driver.get("https://stats.oecd.org/")
driver.maximize_window()

# to click on agriculture and fisheres
driver.find_element(By.XPATH,"/html/body/form/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[2]/span").click()

# to click on environmental indicators
driver.find_element(By.XPATH,"/html/body/form/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[2]/ul/li[3]").click()

# nutrients
driver.find_element(By.XPATH,"/html/body/form/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[2]/ul/li[3]/ul/li[1]/span").click()

# nutriential balance
driver.find_element(By.XPATH, "/html/body/form/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/ul/li[2]/ul/li["
                              "3]/ul/li[1]/ul/li[1]/a[2]").click()
time.sleep(5)

# drop down
driver.find_element(By.XPATH, "/html/body/form/div/div[3]/div[1]/div[4]/div/div[1]/div/div/ul/li[2]/a/span[1]/span[2]").click()
driver.find_element(By.XPATH, "/html/body/form/div/div[3]/div[1]/div[4]/div/div[1]/div/div/ul/li[2]/a/span[1]/span[2]").click()

time.sleep(3)
driver.find_element(By.ID, "ui-menu-0-1").click()
time.sleep(3)
driver.find_element(By.ID, "ui-menu-0-1").click()

time.sleep(3)
driver.find_element(By.XPATH,"/html/body/form/div/div/div[2]")
time.sleep(3)
e=driver.find_element(By.XPATH,"//*[@id=\"dialog-modal\"]")
driver.find_element(By.XPATH,"//input[@id='_ctl12_btnExportCSV']")


