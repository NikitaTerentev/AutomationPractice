#2 задача

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_acc = driver.find_element_by_id("menu-item-50").click()
# reg = driver.find_element_by_id("reg_email").send_keys("gonnatest@bk.ru")
# psw = driver.find_element_by_id("reg_password").send_keys("ntcnbhetv")
# reg = driver.find_element_by_css_selector("[value='Register']").click()
# driver.quit()
# Смысл пароля был в том, чтобы писать не английские слова, я написал просто слово "тестируем" английскими буквами



#3 задача

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# enter = driver.find_element_by_id("menu-item-50").click()
# my_acc = driver.find_element_by_id("username").send_keys("gonnatest@bk.ru")
# password = driver.find_element_by_id("password").send_keys("ntcnbhetv")
# login_in_system = driver.find_element_by_css_selector("[value='Login']").click()
# logout = driver.find_element_by_class_name("woocommerce-MyAccount-navigation-link--customer-logout").click()
# logout = WebDriverWait(driver, 5).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-MyAccount-navigation-link--customer-logout"))
# )
# driver.quit()