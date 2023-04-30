from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

ser = Service(r"C:\Development\\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=op)


driver.get("https://www.google.com")
# driver.close()
