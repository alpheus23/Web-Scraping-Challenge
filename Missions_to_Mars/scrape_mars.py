# import necessary libraries
from splinter import Browser
from bs4 import BeautifulSoup as bs

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    #Create a dictionary of scraped data
    site_info = {}
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
    news_title = content_t.find('a').get_text()

    #Breakdown search for paragraph under title
    search_p = soup.find('li', class_='slide')
    news_p = search_p.find('div', class_='article_teaser_body').get_text()

    print(f"First Article: {news_title}\n")
    print(f"Article Paragraph: {news_p}\n")

    print('-------------------')
    print("Search complete")
    print('-------------------')


    #Navigate to the next site to scrape
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)


    #Navigate site to reach featured image
    browser.links.find_by_partial_text('FULL IMAGE').click()

    #Wait period between next click
    browser.is_element_present_by_text('more info', wait_time=1)

    #Next click
    browser.links.find_by_partial_text('more info').click()


    #HTML object
    html = browser.html
    #Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #Breakdown search for image url
    section_i = soup.find('figure', class_='lede')
    link = section_i.find('a')
    href = link['href']
    image_url = (f'https://www.jpl.nasa.gov{href}')

    #Print image url
    print(f'Image URL: {image_url}\n')

    print('-------------------')
    print("Search complete")
    print('-------------------')


    site_info["News_Title"] = news_title
    site_info["News_Paragraph"] = news_p


    return site_info
