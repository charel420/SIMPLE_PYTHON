from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import hashlib

driver = webdriver.Chrome('chromedriver')
driver.get("WEBSITE URL") 

insert_box = driver.find_element(By.XPATH, 'XPATH of a place to insert')
output_string = driver.find_element(By.XPATH, 'XPATH of text you want to hash ').text
submit_btn = driver.find_element(By.XPATH, 'XPATH of submit button')
md5_encrypting = output_string.encode()
md5_final = hashlib.md5(md5_encrypting).hexdigest()


insert_box.send_keys(md5_final)

submit_btn.click()