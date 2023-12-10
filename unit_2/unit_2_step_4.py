# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# time.sleep(1)
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import math
# import time
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# link = 'http://suninjuly.github.io/explicit_wait2.html'
# browser = webdriver.Chrome()
# browser.get(link)
# price = WebDriverWait(browser, 12).until(
#     EC.text_to_be_present_in_element((By.ID, 'price'), '100')
# )
# book_button = browser.find_element(By.ID, 'book')
# book_button.click()
# x = browser.find_element(By.ID, 'input_value').text
# y = calc(x)
# field = browser.find_element(By.ID, 'answer')
# field.send_keys(y)
# submit_button = browser.find_element(By.ID, 'solve')
# submit_button.click()
# time.sleep(5)
