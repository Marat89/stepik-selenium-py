from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print(y)
browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_id('robotCheckbox').click()
robot = browser.find_element_by_id ("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
robot.click()
option3 = browser.find_element_by_xpath('//button')
option3.click()
time.sleep(10)
browser.quit()
