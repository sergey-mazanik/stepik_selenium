# def test_input_text(expected_result, actual_result):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'

# def test_substring(full_string, substring):
#     assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# class TestForm(unittest.TestCase):
#
#     def test_reg1(self):
#         browser = webdriver.Chrome()
#         link = "http://suninjuly.github.io/registration1.html"
#         browser.get(link)
#         input1 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.first')
#         input1.send_keys('req')
#         input2 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.second')
#         input2.send_keys('req')
#         input3 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.third')
#         input3.send_keys('req')
#         button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#         button.click()
#         time.sleep(1)
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         welcome_text = welcome_text_elt.text
#         self.assertEquals(welcome_text, "Congratulations! You have successfully registered!", "Test has differences")
#
#     def test_reg2(self):
#         browser = webdriver.Chrome()
#         link = "http://suninjuly.github.io/registration2.html"
#         browser.get(link)
#         input1 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.first')
#         input1.send_keys('req')
#         input2 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.second')
#         input2.send_keys('req')
#         input3 = browser.find_element(By.CSS_SELECTOR, 'input[required].form-control.third')
#         input3.send_keys('req')
#         button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#         button.click()
#         time.sleep(1)
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         welcome_text = welcome_text_elt.text
#         self.assertEquals(welcome_text, "Congratulations! You have successfully registered!", "Test has differences")
#
#
# if __name__ == "__main__":
#     unittest.main()
