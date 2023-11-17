# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
#
# закрываем браузер после всех манипуляций
# browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link1 = browser.find_element(By.LINK_TEXT, '224592')
#     link1.click()
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, 'input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, 'last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
#     input1.send_keys('Name')
#     input1 = browser.find_element(By.CLASS_NAME, 'form-control.second')
#     input1.send_keys('Surname')
#     input1 = browser.find_element(By.CLASS_NAME, 'form-control.third')
#     input1.send_keys('Email')
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     #### Заполнение обязательных полей (как в задании) #####
#     # elements = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
#     # for el in elements:
#     #     el.send_keys('required')
#
#     input1 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.first')
#     input1.send_keys('req')
#     input2 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.second')
#     input2.send_keys('req')
#     input3 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.third')
#     input3.send_keys('req')
#
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
