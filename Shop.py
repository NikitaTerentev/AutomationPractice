#4 задача

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
# shop = driver.find_element_by_id("menu-item-40").click()
# book = driver.find_element_by_css_selector("[alt='Mastering HTML5 Forms']").click()
# current_text = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "entry-title"), "HTML5 Forms")
# )
# driver.quit()





#5 задача

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
# shop = driver.find_element_by_id("menu-item-40").click()
# html_3 = driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product-category/html/']").click()
# time.sleep(3)
# html_items = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(html_items) == 3:
#     print("We are good")
# else: print("We dont have 3 items. We actually have: " + str(len(html_items)))
#
# driver.quit()





#6 задача

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
# shop = driver.find_element_by_id("menu-item-40").click()
# orderby = driver.find_element_by_css_selector(".orderby [value='menu_order']")
# check = WebDriverWait(driver, 5).until(
#     EC.element_to_be_selected(orderby)
# )
# orderby_select = driver.find_element_by_class_name("orderby")
# select = Select(orderby_select)
# select.select_by_value("price-desc")
# current_orderby = driver.find_element_by_css_selector(".orderby [value='price-desc']")
# second_check = WebDriverWait(driver, 5).until(
#     EC.element_to_be_selected(current_orderby)
# )
# time.sleep(3)
# driver.quit()





#7 задача

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
# shop = driver.find_element_by_id("menu-item-40").click()
# book = driver.find_element_by_css_selector("[alt='Android Quick Start Guide']").click()
# old_price = driver.find_element_by_tag_name("del").text
# print(old_price)
# assert old_price == "₹600.00"
# book_open = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']"))
# )
# book_open.click()
# close = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
# )
# close.click()
# time.sleep(3)
# driver.quit()





#8 задача

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
# shop = driver.find_element_by_id("menu-item-40").click()
# add = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(3)
# item = driver.find_element_by_class_name("cartcontents").text
# assert item == "1 Item"
# amount = driver.find_element_by_class_name("amount").text
# assert amount == "₹180.00"
# item1 = driver.find_element_by_class_name("cartcontents").click()
# sub = WebDriverWait(driver, 5).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "cart-subtotal"))
# )
# sub_text = driver.find_element_by_css_selector("[data-title='Subtotal']").text
# assert sub_text == "₹180.00"
# total = WebDriverWait(driver,5).until(
#     EC.visibility_of_element_located((By.TAG_NAME, "strong"))
# )
# total_text = driver.find_element_by_tag_name("strong").text
# assert total_text == "₹189.00"
# time.sleep(3)
# driver.quit()





#9 задача

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
# shop = driver.find_element_by_id("menu-item-40").click()
# add = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 300);")
# second_add = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
# time.sleep(2)
# item = driver.find_element_by_class_name("cartcontents").click()
# time.sleep(2)
# remove = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(2)
# undo = driver.find_element_by_partial_link_text("Undo?").click()
# time.sleep(2)
# quan = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# quantity = quan.clear()
# quantity_new = quan.send_keys(3)
# update = driver.find_element_by_name("update_cart").click()
# time.sleep(2)
# #изначально пытался взять атрибут у quan, т. написать q = quan.get_attribute("value"), но почему то получалась ошибка
# #пришлось дублировать код
# q = driver.find_element_by_css_selector("[value='3']")
# quantity_value = q.get_attribute("value")
# assert quantity_value == "3"
# time.sleep(2)
# apply = driver.find_element_by_css_selector("[value='Apply Coupon']").click()
# time.sleep(2)
# alert = driver.find_element_by_class_name("woocommerce-error")
# alert_text = alert.text
# assert alert_text == "Please enter a coupon code."
# time.sleep(3)
# driver.quit()





#10 задача

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
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# add = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(2)
# item = driver.find_element_by_class_name("cartcontents").click()
# checkout = WebDriverWait(driver, 25).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))
# )
# checkout.click()
# first_name = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name"))
# )
# first_name.send_keys("Abobus")
# last_name = driver.find_element_by_id("billing_last_name").send_keys("Doggo")
# email = driver.find_element_by_id("billing_email").send_keys("doggo@mail.ru")
# phone = driver.find_element_by_id("billing_phone").send_keys("123456789")
# driver.execute_script("window.scrollBy(0, 500);")
# country = driver.find_element_by_tag_name("b").click()
# country_text = driver.find_element_by_class_name("select2-input").send_keys("uk")
# time.sleep(2)
# current_country = driver.find_elements_by_id("select2-result-label-5596")
# #очень долго вытался разобраться, но так и не понял, как выбрать второй элемент
# #если после id дописать .click, то программа падает, если написать element без S, то элемент вообще не находится
# city = driver.find_element_by_id("billing_city").send_keys("Abobus city")
# state = driver.find_element_by_id("billing_state").send_keys("US")
# post_code = driver.find_element_by_id("billing_postcode").send_keys("123333")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(5)
# pay_method = driver.find_element_by_id("payment_method_cheque").click()
# order = driver.find_element_by_id("place_order").click()
# thanks = WebDriverWait(driver, 5).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "woocommerce-thankyou-order-received"))
# )
# payment_method = WebDriverWait(driver,5).until(
#     EC.visibility_of_element_located((By.LINK_TEXT, "Check Payments"))
# )
# time.sleep(5)
# driver.quit()