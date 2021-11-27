import requests
from bs4 import BeautifulSoup
import lxml
import re

url = 'http://books.toscrape.com/'
dir = '/home/garrotero/category_page_data/'

def create_file_with_url_content(url, filename):
    features = "lxml"
    request = requests.get(url)
    content = request.text
    scraping_file = open(dir + filename, 'w')
    soup = BeautifulSoup(content, features)
    soup = str(soup)
    scraping_file.write(soup)
    scraping_file.close()
    scraping_file = open(dir + filename, 'a')
    scraping_file.write('FULL WEB ADDRESS: {}'.format(url))
    scraping_file.close()

create_file_with_url_content(url, 'category_page_data_0.txt')

def list_of_hrefs(file, href_file_name):
    list_of_hrefs = []
    for book in open(file, 'r').readlines():
        if 'a href' in book:
            list_of_hrefs.append(book)        
    href_file = open(dir + href_file_name, 'w')
    for href in list_of_hrefs:
        href_file.write(href)
    href_file.close()

list_of_hrefs(dir +'category_page_data_0.txt', 'href_file.txt')

def string_search(string):
    start = string.find('a href="') + len('a href="')
    end = string.find('">')
    extension = ''
    for char in string[start:end]:
        extension += char
    return extension

#https://books.toscrape.com/

def list_of_categories():
    list_of_categories = []
    href_file = open('href_file.txt', 'r')
    for href in href_file.readlines():
        if 'catalogue/category' in href:
            list_of_categories.append('https://books.toscrape.com/' + string_search(href))
    return list_of_categories

number = 1
list_of_files = []
for url_page in list_of_categories():
    create_file_with_url_content(url_page, 'category_page_data_{}.txt'.format(number))
    list_of_files.append('category_page_data_{}.txt'.format(number))
    number += 1
print(list_of_files)

import os
os.remove(dir + 'category_page_data_1.txt')

for filename in os.listdir(dir):
    if 'category_page_data_' in filename and not filename == 'category_page_data_0':
        list_of_hrefs(dir + filename, 'hrefs_' + filename)

list_of_href_matches = []
for filename in os.listdir('/home/garrotero/category_page_data'):
    if filename.startswith('hrefs'):
        opened_href_file = open(dir + filename, 'r')
        for fileline in opened_href_file.readlines():
            print(fileline)
            fileline = str(fileline)
            match = re.search(pattern='(?<=a href="../../../).*(?=" title)', string=fileline)
            if match:
                print(match.group())
