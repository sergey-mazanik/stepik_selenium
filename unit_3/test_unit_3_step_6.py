# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import cred
# from time import sleep, time
# import math
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# link = "https://stepik.org/lesson/236895/step/1"
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
#          'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
#          'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
#          'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']
#
#
# @pytest.mark.parametrize('urls', links)
# class TestNLO:
#     def test_open_links(self, browser, urls):
#         find_time = str(math.log(int(time())))
#         link = urls
#         browser.get(link)
#         sleep(3)
#         login_button = browser.find_element(By.ID, 'ember35')
#         login_button.click()
#         sleep(3)
#         input_email_field = browser.find_element(By.ID, 'id_login_email')
#         input_email_field.send_keys(cred.username)
#         input_password_field = browser.find_element(By.ID, 'id_login_password')
#         input_password_field.send_keys(cred.password)
#         login_button_popup = browser.find_element(By.XPATH, '//button[@type="submit"]')
#         login_button_popup.click()
#         sleep(5)
#         answer_field = browser.find_element(By.XPATH, '//textarea')
#         answer_field.clear()
#         sleep(2)
#         answer_field.send_keys(find_time)
#         sleep(2)
#         confirm_button = WebDriverWait(browser, 5).until(
#             EC.element_to_be_clickable((By.XPATH, '//button[@class="submit-submission"]')))
#         confirm_button.click()
#         sleep(5)
#         message = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]')
#         print(message.text)
#         assert 'Correct!' in message.text, f'{message.text}'
