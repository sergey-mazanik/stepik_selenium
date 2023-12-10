# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link = 'http://suninjuly.github.io/alert_accept.html'
# browser = webdriver.Chrome()
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser.get(link)
#     input1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     input1.click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     x = browser.find_element(By.ID, 'input_value').text
#     y = calc(x)
#     field = browser.find_element(By.ID, 'answer')
#     field.send_keys(y)
#     input2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     input2.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link = 'http://suninjuly.github.io/redirect_accept.html'
# browser = webdriver.Chrome()
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser.get(link)
#     input1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     input1.click()
#     new_window = browser.window_handles[1]
#     first_window = browser.window_handles[0]
#     browser.switch_to.window(new_window)
#     x = browser.find_element(By.ID, 'input_value').text
#     y = calc(x)
#     field = browser.find_element(By.ID, 'answer')
#     field.send_keys(y)
#     input2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     input2.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()
