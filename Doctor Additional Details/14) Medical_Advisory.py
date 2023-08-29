from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.maximize_window()
actions = ActionChains(driver)

driver.get("http://165.22.217.185")

driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()

driver.implicitly_wait(5)
driver.get("http://165.22.217.185/layout/doctorDetail/9")
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//*[@id='pr_id_14_header_0']").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//span[@class='btn btn-primary mb-3 float-end']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@name='MedicalAdvisoryOrSpeakerPurpose']").send_keys(" Awareness")
driver.find_element(By.XPATH, "//input[@name='MedicalAdvisoryOrSpeakerAmount'] ").send_keys(" 10000")
driver.find_element(By.XPATH, "//input[@name='MedicalAdvisoryOrSpeakerCompanyName'] ").send_keys("QB")
actions.send_keys(Keys.TAB).send_keys("21/08/2023").send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
actions.send_keys("21/08/2023").send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
driver.find_element(By.XPATH, "//input[@name='MedicalAdvisoryOrSpeakerBussinessValue'] ").send_keys("500000")
driver.find_element(By.XPATH, " //textarea[@name='Remarks']").send_keys("Speaker")
driver.find_element(By.XPATH, " //*[@id='pr_id_19_header_0']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, " //input[@name='MedicalAdvisoryOrSpeakerCompanyAddressLine1']").send_keys("Ahmedabad")
driver.find_element(By.XPATH, " //input[@name='MedicalAdvisoryOrSpeakerCompanyAddressLine2']").send_keys("Ahmedabad")
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
time.sleep(1)
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
driver.find_element(By.XPATH, "//button[@type='submit'] ").click()
