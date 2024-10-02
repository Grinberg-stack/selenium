import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

driver.get('https://www.facebook.com/')
driver.find_element(By.ID, 'email').send_keys('amit')
driver.find_element(By.ID, 'pass').send_keys('amit')
driver.find_element(By.NAME, 'login').click()

input()
