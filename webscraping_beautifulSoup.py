import requests
from bs4 import BeautifulSoup
import lxml
import re
import mysql.connector as mysql
import json

def get_html_content(url):
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def get_html_data(url):
    category_list = []
    soup = get_html_content(url)
    tag = soup.find_all('a', href=True)
    for t in tag:
        if 'category' in t.attrs['href'] and 'books_1' not in t.attrs['href']:
            category_list.append('https://books.toscrape.com/' + t.attrs['href'])      
    return category_list 
         
categories = get_html_data('https://books.toscrape.com/')

def check_for_other_pages(category):
    soup = get_html_content(category)
    page = soup.find('li', attrs={'class': 'current'})
    if page != None:
        return page.text.split()[-1]

def create_list_of_other_pages_books(category, pages):
    list_of_further_pages_urls = []
    for page in range(2, int(pages) + 1):
        new_category_page = category.replace('index', 'page-{}'.format(page))
        list_of_further_pages_urls.append(new_category_page)
    return list_of_further_pages_urls

def get_book_list(url_list):
    book_list = []
    for category in url_list:
        soup = get_html_content(category)
        a_tag = soup.findAll('a', href=True)
        for i in a_tag:
            if i.attrs['href'].startswith('../../../') and len(i.attrs) == 1 and not i.attrs['href'].startswith('../../../../'):
                book_url = ('https://books.toscrape.com/catalogue/' + i.attrs['href'].replace('../../../', ''))
                book_list.append(book_url)
    return book_list

complete_book_list = []
for category in categories:
    url_list = []
    url_list.append(category)
    number_of_pages = check_for_other_pages(category)
    if number_of_pages:
        url_list.extend(create_list_of_other_pages_books(category, number_of_pages))
    complete_book_list.extend(get_book_list(url_list))


for book_url in complete_book_list:
    book_urls_file = open('complete_book_list_urls.txt', 'a')
    book_urls_file.write(book_url + '\n')
book_urls_file.close()
    
