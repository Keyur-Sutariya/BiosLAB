from selenium import webdriver
from PIL import Image
from Screenshot import Screenshot

driver = webdriver.Firefox()
driver.get("https://www.google.co.in")
driver.maximize_window()
for i in range(1, 3):
    driver.save_screenshot(f"google{i}.png")
    driver.get("https://www.youtube.com")
    i = i + 1
