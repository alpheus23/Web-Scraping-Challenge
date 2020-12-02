# import necessary libraries
from splinter import Browser
from bs4 import BeautifulSoup as bs

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    #Create a dictionary of scraped data
    data_scrape = {}
    #Initialize browser
    browser = init_browser()

    #URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)


    #HTML object
    html = browser.html
    #Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #Breakdown search for first article title
    search_t = soup.find('li', class_='slide')
    content_t = search_t.find('div', class_='content_title')
    news_title = content_t.find('a').text

    #Breakdown search for paragraph under title
    search_p = soup.find('li', class_='slide')
    news_p = search_p.find('div', class_='article_teaser_body').text

    print(f"First Article: {news_title}\n")
    print(f"Article Paragraph: {news_p}\n")

    print('-------------------')
    print("Search complete")
    print('-------------------')


    data_scrape["News Title"] = news_title
    data_scrape["News paragraph"] = news_p


    return data_scrape