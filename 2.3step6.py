from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
print(y)
browser.find_element_by_id('answer').send_keys(y)

time.sleep(10)