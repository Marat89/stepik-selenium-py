from selenium import webdriver
import time
import os
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
name = browser.find_element_by_name("firstname")
name.send_keys("Вася")
second_name = browser.find_element_by_name("lastname")
second_name.send_keys("Я")
email = browser.find_element_by_name("email")
email.send_keys("Снеслася")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "321.txt"
file_path = os.path.join(current_dir, file_name)
file_uploud = browser.find_element_by_id("file")
file_uploud.send_keys(file_path)
time.sleep(10)