import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = 'https://old.reddit.com/r/aliens/comments/14rp7w9/from_the_late_2000s_to_the_mid2010s_i_worked_as_a/'
driver.get(link)

time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 999999999999999999999999999999999999);")
time.sleep(0.5)
elements = driver.find_elements(By.TAG_NAME,"p")

for element in elements:
    if not (element.text == '' or element.text.__contains__('[–]')):
        print(element.text)

driver.quit()