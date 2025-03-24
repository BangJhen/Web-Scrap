from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.rumah123.com/sewa/cari/?q=bandung")

nama_tempat = []

elements = driver.find_elements(by=By.CLASS_NAME, value="intersection-card-container")

for el in elements:
    name_section = el.find_element(By.CLASS_NAME, "card-featured__middle-section")
    name = name_section.find_element(By.TAG_NAME, "h2")
    nama_tempat.append(name.text)p3

time.sleep(2)
driver.quit()