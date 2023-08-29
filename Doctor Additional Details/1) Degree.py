import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://165.22.217.185")
driver.find_element("name", "LoginId").send_keys("employee")
driver.find_element("name", "Password").send_keys("123123123")
driver.find_element(By.XPATH, "//div[button/@type='submit']").click()
time.sleep(2)
driver.get("http://165.22.217.185/layout/doctorDetail/9")
time.sleep(2)
driver.find_element(By.ID, "pr_id_1_header_0").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[normalize-space()='Add Degree'] ").click()
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).send_keys(Keys.TAB).perform()
actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).send_keys(Keys.TAB).perform()
driver.find_element(By.XPATH, " //input[@name='DegreeAdmissionYear']").send_keys('2012')
driver.find_element(By.XPATH, " //input[@name='DegreePassOutYear']").send_keys('2016')
driver.find_element(By.XPATH, " //input[@name='DegreeCollege']").send_keys('Nirma')
driver.find_element(By.XPATH, " //input[@name='DegreeRegistrationNumber']").send_keys('15213132456')

driver.find_element(By.ID, "pr_id_18_header_0").click()
time.sleep(2)
driver.find_element(By.XPATH, " //input[@name='DegreeRegistrationNumber']").send_keys('123321123')
driver.find_element(By.XPATH, " //input[@name='DegreeCollegeAddressLine1']").send_keys('Chandkheda')
driver.find_element(By.XPATH, " //input[@name='DegreeCollegeAddressLine2']").send_keys('Ahmedabad')
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).send_keys(Keys.TAB).perform()
time.sleep(5)
actions.send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
time.sleep(5)
actions.send_keys(Keys.ESCAPE)
time.sleep(5)
driver.find_element(By.ID, "pr_id_12").click()
time.sleep(5)

# driver.find_element(By.CSS_SELECTOR, "div[id='pr_id_12_content_0'] span[class='btn btn-primary mb-3 float-end']").click()

# driver.find_element(By.XPATH, "//button[@class='btn btn-outline-primary mt-2 mx-2']").click()
# actions.send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.DOWN).send_keys(Keys.ENTER).send_keys(Keys.TAB).perform()
# driver.find_element(By.XPATH, "//textarea[@name='Remarks']").send_keys("Remarks ")


time.sleep(3)
