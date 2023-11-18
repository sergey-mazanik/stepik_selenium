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
