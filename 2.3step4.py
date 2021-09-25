
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_xpath("//div/button").click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_xpath("//div/button").click()
print(browser.switch_to.alert.text)