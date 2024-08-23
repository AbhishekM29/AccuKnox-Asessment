from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("localhost:8080")
driver.maximize_window()
msg_1= driver.find_element(By.TAG_NAME,"h1")
msg_text=msg_1.text
if (msg_text=="Hello from the Backend!"):
    print("Test Passed Successfully")
elif(msg_text=="Hello, World!" or ""):
    print("Test was Unsuccessfull")
driver.close()
