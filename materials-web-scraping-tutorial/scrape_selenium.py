import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = 'https://old.reddit.com/r/aliens/comments/14rp7w9/from_the_late_2000s_to_the_mid2010s_i_worked_as_a/'
driver.get(link)
run = True
time.sleep(1)
driver.execute_script("window.scrollTo(0, 999999999999999999999999999999999999);")
try:
    while(run):
        time.sleep(1)
        button_elements = driver.find_elements(By.CLASS_NAME,"button")
        for button in button_elements:
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            button.click()
            time.sleep(2)
        button_elements = driver.find_elements(By.CLASS_NAME,"button")
        if(len(button_elements) == 0):
            run = False
        time.sleep(20)
except:
    pass

elements = driver.find_elements(By.TAG_NAME,"p")

for element in elements:
    if not (element.text == '' or element.text.__contains__('[–]')):
        print(element.text)

driver.quit()