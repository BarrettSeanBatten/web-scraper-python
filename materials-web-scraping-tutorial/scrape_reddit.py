import requests
from bs4 import BeautifulSoup
from lxml import etree


def scrape_conversation(href):
    # URL of the Reddit page you want to scrape
    url = 'https://www.reddit.com' + href

    # Send a GET request to the URL and retrieve the HTML content
    response = requests.get(url)
    html_content = response.content

    # Create a BeautifulSoup object by parsing the HTML content
    soup = BeautifulSoup(html_content, 'lxml')

    # Convert BeautifulSoup object to lxml etree for XPath operations
    html_tree = etree.HTML(str(soup))

    # Use XPath to find the elements that contain the conversations
    conversation_elements = html_tree.xpath('//*[@id="t3_14rp7w9-post-rtjson-content"]/p/text()')

    #//*[@id="t3_14rp7w9-post-rtjson-content"]

    # Iterate over the conversation elements and extract the desired information
    for conversation in conversation_elements:    
        print(conversation)
        # # Extract the content of the conversation using XPath
        # content = conversation.xpath('.//div[@class="s1ka5y82-1"]/text()')[0].strip()
        
        # # Print the title and content of the conversation
        # print(content)
        # print('\n---\n')
        
        
def main():
    href = '/r/aliens/comments/14rp7w9/from_the_late_2000s_to_the_mid2010s_i_worked_as_a/'
    scrape_conversation(href)

if __name__ == "__main__":
    main()
