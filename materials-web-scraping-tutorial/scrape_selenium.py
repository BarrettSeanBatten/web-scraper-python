import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys
import json

import username_generate

# {sub_name: [(og_post, list of comments, user_name)]}   How to store the data, add the username
# cut it at thrid level comment
# limit to certain number of comments per post (300)
# 100 post limit per subreddit

def scrape(link):
    subreddit = link.split('/')[4]
    name = link.split('/')[7]
    
    link2 = link.replace('old','www',1)
    
    driver2 = webdriver.Chrome()
    driver2.get(link2)
    run = True
    time.sleep(2)
    title = driver2.find_element(By.XPATH, '/html/body/shreddit-app/div/div[2]/shreddit-post/div[2]')
    name = driver2.find_element(By.XPATH, '/html/body/shreddit-app/div/div[2]/shreddit-post/div[1]/span[1]/div/div/span[1]/span/div/faceplate-hovercard/faceplate-tracker/a')
    title = title.text
    name = name.text
    driver2.quit()
    driver = webdriver.Chrome()
    driver.get(link)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 999999999999999999999999999999999999);")
    count = 0
    count2 = 0
   # try:
    while(run):
        try:
            time.sleep(2)
            button_elements = driver.find_elements(By.CLASS_NAME,"button")
            if(len(button_elements) > 0):
                driver.execute_script("arguments[0].scrollIntoView(true);", button_elements[len(button_elements)-1])
                button_elements[len(button_elements)-1].click()
                count2 += 1
            time.sleep(4)
            button_elements = driver.find_elements(By.CLASS_NAME,"button")
            
            if(len(button_elements) == 0 or count2 > 10):
                run = False
        except:
            run = False
    
    
    comments_list = []
    # original_post = driver.find_elements(By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div/p')
    # if len(original_post) > 0:
    #     original_post = original_post[0].text
    # else:
    #     original_post = ' '
    # original_poster = driver.find_elements(By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div/p[2]/a')[0].text
    first_level_comments = driver.find_elements(By.XPATH,"/html/body/div/div/div/div/div/form/div/div")
    first_level_points = driver.find_elements(By.XPATH,"/html/body/div/div/div/div/div/p/span[3]")
    for i in range(len(first_level_comments)):
        if count >= 300:
            #return (original_post, original_poster, comments_list)
            return [subreddit,(title, name, comments_list)]
        first_comment = first_level_comments[i].find_elements(By.TAG_NAME, "p")
        first_text = ''
        for comment in first_comment:
            first_text += comment.text + ' '
        comments_list.append((username_generate.generate_username(), first_text))
        count += 1
        second_level_xpath = "/html/body/div[4]/div[2]/div[3]/div[" + str(1 + 2*i) + "]/div[3]/div/div[1]/div[2]/form/div/div"
        second_points_xpath = "/html/body/div[4]/div[2]/div[3]/div[" + str(1 + 2*i) + "]/div[3]/div/div[1]/div[2]/p/span[3]"
        third_level_xpath = "/html/body/div[4]/div[2]/div[3]/div[" + str(1 + 2*i) + "]/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/form/div/div"
        third_points_xpath = "/html/body/div[4]/div[2]/div[3]/div[" + str(1 + 2*i) + "]/div[3]/div/div[1]/div[2]/div/div[1]/div[2]/p/span[3]"
        second_comments = driver.find_elements(By.XPATH, second_level_xpath)
        if len(second_comments) > 0:
            second_level_points = driver.find_element(By.XPATH, second_points_xpath)
            second_text = ''
            second_comment = second_comments[0].find_elements(By.TAG_NAME, 'p')
            for comment in second_comment:
                second_text += comment.text + ' '
            comments_list.append((username_generate.generate_username(), second_text))
            count += 1
            third_comments = driver.find_elements(By.XPATH, third_level_xpath)
            if len(third_comments) > 0:
                third_level_points = driver.find_element(By.XPATH, third_points_xpath)
                third_text = ''
                third_comment = third_comments[0].find_elements(By.TAG_NAME, 'p')
                for comment in third_comment:
                    third_text += comment.text + ' '
                comments_list.append((username_generate.generate_username(), third_text))
                count += 1
        
    driver.quit()
    #return (original_post, original_poster, comments_list)
    return [subreddit,(title, name, comments_list)]
    
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
                if href.startswith('https://old.reddit.com/r/'):
                    hrefs.append(href)
                    count += 1
                elif href.startswith('https://www.reddit.com/r/'):
                    new_href = href.replace('://www', '://old')
                    hrefs.append(new_href)
                    count += 1
                if count >= num:
                    return hrefs
            except:
                pass
        next_button = driver.find_elements(By.CLASS_NAME, "next-button")
        if not len(next_button) == 0:
            button = next_button[0].find_element(By.TAG_NAME, "a")
            button.click()
            time.sleep(2)
        else:
            return hrefs
    return hrefs
        
        
    
def main():
    dict = {}
    
    # pass link to desired reddit page/subreddit as first command line argument
    # pass number of desired reddit pages to scrape as second command line argument
    subreddit = sys.argv[1]
    num = int(sys.argv[2])
    hrefs = generateHrefs(num,subreddit)
    for href in hrefs:
        comments = scrape(href)
        #print(comments)
        
        if dict.get(comments[0]):
            dict.get(comments[0]).append(comments[1])
        else:
            dict[comments[0]] = []
            dict[comments[0]].append(comments[1])
            
    # for key, value in dict.items():
    #     print(key, ":", value)
        
    json_data = json.dumps(dict)
    print(json_data)

    
if __name__ == "__main__":
    main()