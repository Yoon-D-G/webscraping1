import requests
from bs4 import BeautifulSoup
import lxml

url = 'http://books.toscrape.com/'

def create_file_with_url_content(url, filename):
    req = requests.get(url)
    content = req.text
    scraping_file = open(filename, 'w')
    soup = BeautifulSoup(content)
    soup = str(soup)
    scraping_file.write(soup)
    scraping_file.close()

create_file_with_url_content(url, 'file_content.txt')
