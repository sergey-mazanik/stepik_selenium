# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
#
# try:
#     link = "https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     first_element = int(browser.find_element(By.CSS_SELECTOR, 'span[id="num1"]').text)
#     second_element = int(browser.find_element(By.CSS_SELECTOR, 'span[id="num2"]').text)
#     summa = first_element + second_element
#
#     select = Select(browser.find_element(By.TAG_NAME, 'select'))
#     select.select_by_value(f'{str(summa)}')
#     submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     submit_button.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# time.sleep(3)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()


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
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
#     x = x_element.text
#     y = calc(x)
#     field = browser.find_element(By.ID, 'answer')
#     browser.execute_script('return arguments[0].scrollIntoView(true);', field)
#     field.send_keys(y)
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
# import os
#
# link = 'http://suninjuly.github.io/file_input.html'
# browser = webdriver.Chrome()
# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'file.txt')
#
# try:
#     browser.get(link)
#     input1 = browser.find_element(By.NAME, 'firstname')
#     input1.send_keys('firstname')
#     input2 = browser.find_element(By.NAME, 'lastname')
#     input2.send_keys('lastname')
#     input3 = browser.find_element(By.NAME, 'email')
#     input3.send_keys('test@test.com')
#     input4 = browser.find_element(By.ID, 'file')
#     input4.send_keys(file_path)
#     input5 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#     input5.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()
