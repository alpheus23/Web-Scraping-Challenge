# import necessary libraries
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd

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


    #Navigate to the next site to scrape
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)


    #Click header to navigate to image location
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()


    #HTML object
    html = browser.html
    #Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #Obtain Hemisphere Title
    div_t = soup.find('div', class_='content')
    cerb_title = div_t.find('h2', class_='title').text

    print(f'Hemisphere Title: {cerb_title}\n')

    #Obtain resolution for Cerberus Hemisphere
    div_i = soup.find('img', class_='wide-image')
    img_src = div_i['src']
    cerb_image_url = (f'https://astrogeology.usgs.gov/{img_src}')

    print(f'Hemisphere Image: {cerb_image_url}\n')

    print('-------------------')
    print("Search complete")
    print('-------------------')


    #Reload the previous page
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)


    #Click header to navigate to image location
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()


    #HTML object
    html = browser.html
    #Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #Obtain Hemisphere Title
    div_t = soup.find('div', class_='content')
    schi_title = div_t.find('h2', class_='title').text

    print(f'Hemisphere Title: {schi_title}\n')

    #Obtain resolution for Cerberus Hemisphere
    div_i = soup.find('img', class_='wide-image')
    img_src = div_i['src']
    schi_image_url = (f'https://astrogeology.usgs.gov/{img_src}')

    print(f'Hemisphere Image: {schi_image_url}\n')

    print('-------------------')
    print("Search complete")
    print('-------------------')


    #Reload the previous page
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)


    #Click header to navigate to image location
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()


    #HTML object
    html = browser.html
    #Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #Obtain Hemisphere Title
    div_t = soup.find('div', class_='content')
    syr_title = div_t.find('h2', class_='title').text

    print(f'Hemisphere Title: {syr_title}\n')

    #Obtain resolution for Cerberus Hemisphere
    div_i = soup.find('img', class_='wide-image')
    img_src = div_i['src']
    syr_image_url = (f'https://astrogeology.usgs.gov/{img_src}')

    print(f'Hemisphere Image: {syr_image_url}\n')

    print('-------------------')
    print("Search complete")
    print('-------------------')


    #Reload the previous page
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)


    #Click header to navigate to image location
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()


    #HTML object
    html = browser.html
    #Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    #Obtain Hemisphere Title
    div_t = soup.find('div', class_='content')
    val_title = div_t.find('h2', class_='title').text

    print(f'Hemisphere Title: {val_title}\n')

    #Obtain resolution for Cerberus Hemisphere
    div_i = soup.find('img', class_='wide-image')
    img_src = div_i['src']
    val_image_url = (f'https://astrogeology.usgs.gov/{img_src}')

    print(f'Hemisphere Image: {val_image_url}\n')

    print('-------------------')
    print("Search complete")
    print('-------------------')

    
    site_info["News_Title"] = news_title
    site_info["News_Paragraph"] = news_p
    site_info["Image_URL"] = image_url
    site_info["Cerb_URL"] = cerb_image_url
    site_info["Schi_URL"] = schi_image_url
    site_info["Syr_URL"] = syr_image_url
    site_info["Val_URL"] = val_image_url

    return site_info