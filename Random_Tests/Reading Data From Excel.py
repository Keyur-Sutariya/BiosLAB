import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
#configure workbook path
book = openpyxl.load_workbook("/home/tipl-pc-21/Desktop/Usernames.xlsx")
#get active sheet
sheet = book.active
#get cell address of email within active sheet
email = sheet.cell (row = 3, column = 1)
#get cell address of password within active sheet
password = sheet.cell (row = 3, column = 2)

#get values
email_stored = email.value
passw = password.value
driver = webdriver.Firefox()
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://practicetestautomation.com/practice-test-login/")
#identify element
login_email = driver.find_element(By.XPATH,"//input[@id='username']")
#enter email obtained from excel
login_email.send_keys(email_stored)
login_pass = driver.find_element(By.XPATH, " //input[@id='password']")
#enter password obtained from Excel
login_pass.send_keys(passw)
#get values entered
s = login_email.get_attribute("value")
t = login_pass.get_attribute("value")

driver.find_element(By.XPATH, " //button[@id='submit']").click()
print("Email is: ")
print(s)
print("Password is: ")
print(t)

while True:
    pass
#browser quit
driver.quit()












