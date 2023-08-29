from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
actions = ActionChains(driver)

check = driver.current_url

driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

driver.implicitly_wait(5)
driver.get("http://165.22.217.185/layout/doctorDetail/9")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//*[@id='pr_id_8_header_0']").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, " //span[@class='btn btn-primary mb-3 float-end']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@name='TypeOfSocialActivity']").send_keys("KKK")
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, "//input[@name='SocialActivityNoOfParticipants']").send_keys("10")
driver.find_element(By.XPATH, "//input[@name='SocialActivityVenue']").send_keys("KKK")
driver.find_element(By.XPATH, "//input[@name='SocialActivityAmountSpent']").send_keys("10000")
driver.find_element(By.XPATH, "//input[@name='SocialActivitySponsors']").send_keys("KKK")
driver.find_element(By.XPATH, "//textarea[@name='Remarks']").send_keys("KKK")
driver.find_element(By.XPATH, "//textarea[@name='SocialActivityDescription']").send_keys("KKK")
actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

driver.find_element(By.XPATH, "//input[@name='SocialActivityAddressLine1']").send_keys("KKK")
driver.find_element(By.XPATH, "//input[@name='SocialActivityAddressLine2']").send_keys("KKK")
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
time.sleep(2)
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
