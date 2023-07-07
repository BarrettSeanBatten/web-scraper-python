import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.reddit.com/r/aliens/comments/14rp7w9/from_the_late_2000s_to_the_mid2010s_i_worked_as_a/');

time.sleep(2)

#driver.find_element(By.CLASS_NAME, "m-0").click()
driver.execute_script("window.scrollTo(0, 9999999999999999999999999999999999999999999999999);")

time.sleep(1)

elements = driver.find_elements(By.TAG_NAME,"p")

for element in elements:
    if not element.text == '':
        print(element.text)

driver.quit()