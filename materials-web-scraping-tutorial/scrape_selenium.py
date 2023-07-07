import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys



def scrape(link):
    subreddit = link.split('/')[4]
    name = link.split('/')[7]
    file_path = 'output/' + subreddit
    os.makedirs(file_path, exist_ok=True)
    
    file_path += '/' + name + '.txt'
    if os.path.exists(file_path):
        return
    
    file = open(file_path, 'w')
    file.write(link + '\n')
    driver = webdriver.Chrome()
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
            file.write(element.text)
            print(element.text)

    file.close()
    driver.quit()
    
#generates
def generateHrefs(num,link):
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(2)
    count = 0
    hrefs = []
    while(count <= num):
        elements = driver.find_elements(By.CLASS_NAME, "title")
        for element in elements:
            try:
                title = element.find_element(By.TAG_NAME, "a")
                href = title.get_attribute('href')
                print(href)
                if href.startswith('https://old.reddit.com/r/'):
                    hrefs.append(href)
                    count += 1
                if count >= num:
                    return hrefs
            except:
                pass
        next_button = driver.find_element(By.CLASS_NAME, "next-button")
        button = next_button.find_element(By.TAG_NAME, "a")
        button.click()
        time.sleep(10)
        
    return hrefs
        
        
    
def main():
    # pass link to desired reddit page/subreddit as first command line argument
    # pass number of desired reddit pages to scrape as second command line argument
    subreddit = sys.argv[1]
    num = int(sys.argv[2])
    hrefs = generateHrefs(num,subreddit)
    for href in hrefs:
        scrape(href)

    
if __name__ == "__main__":
    main()