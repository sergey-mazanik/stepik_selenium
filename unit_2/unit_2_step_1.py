# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
#     x = x_element.text
#     y = calc(x)
#
#     input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
#     input1.send_keys(y)
#     time.sleep(1)
#     input2 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
#     input2.click()
#     time.sleep(1)
#     input3 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
#     input3.click()
#     time.sleep(1)
#     input4 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     input4.click()
#     time.sleep(1)
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     link = "https://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     find_treasure = browser.find_element(By.CSS_SELECTOR, 'img[id="treasure"]')
#     x_element = find_treasure.get_attribute('valuex')
#     y = calc(x_element)
#
#     input1 = browser.find_element(By.CSS_SELECTOR, 'input[id="answer"]')
#     input1.send_keys(y)
#     input2 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
#     input2.click()
#     input3 = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
#     input3.click()
#     input4 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     input4.click()
#     time.sleep(1)
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
