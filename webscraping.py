import requests
from bs4 import BeautifulSoup
import lxml
import re
import mysql.connector as mysql

url = 'http://books.toscrape.com/'
separate_category_dir = '/home/garrotero/separate_category_data.txt/'
dir = '/home/garrotero/category_page_data/'
book_htmls_dir = '/home/garrotero/book_htmls/'

def create_file_with_url_content(url, filename, dir):
    request = requests.get(url)
    content = request.text
    scraping_file = open(dir + filename, 'w')
    soup = BeautifulSoup(content)
    soup = str(soup)
    scraping_file.write(soup)
    scraping_file.close()
    scraping_file = open(dir + filename, 'a')
    scraping_file.write('FULL WEB ADDRESS: {}'.format(url))
    scraping_file.close()

create_file_with_url_content(url, 'category_page_data_0.txt', separate_category_dir)
def list_of_hrefs(file, href_file_name):
    list_of_hrefs = []
    for book in open(file, 'r').readlines():
        if 'a href' in book:
            list_of_hrefs.append(book)        
    href_file = open(separate_category_dir + href_file_name, 'w')
    for href in list_of_hrefs:
        href_file.write(href)
    href_file.close()
    return list_of_hrefs

list_of_hrefs(separate_category_dir + 'category_page_data_0.txt', 'href_file.txt')

def string_search_1(string):
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
            list_of_categories.append('https://books.toscrape.com/' + string_search_1(href))
    return list_of_categories

def string_search(string, start_sequence, end_sequence):
    start = string.find(start_sequence) + len(start_sequence)
    end = string.find(end_sequence)
    extension = ''
    for char in string[start:end]:
        extension += char
    return extension

dir = '/home/garrotero/category_page_data/'

list_of_multiple_pages = []
file_and_pages_tuple = (['category_page_data_3.txt', '2'], ['category_page_data_4.txt', '2'], ['category_page_data_5.txt', '4'], ['category_page_data_8.txt', '2'], ['category_page_data_10.txt', '4'], ['category_page_data_11.txt', '2'], ['category_page_data_13.txt', '6'], ['category_page_data_15.txt', '8'], ['category_page_data_18.txt', '4'], ['category_page_data_19.txt', '3'], ['category_page_data_21.txt', '3'], ['category_page_data_33.txt', '2'])
for list in file_and_pages_tuple:
    category_file_open = open(dir + list[0], 'r')
    for line in category_file_open.readlines():
        if 'FULL WEB ADDRESS' in line:
            url = string_search(line, 'FULL WEB ADDRESS: ', 'index.html')
            for i in range(2, int(list[1]) + 1):
                list_of_multiple_pages.append(url + 'page-{}.html'.format(i))

def put_url_data_into_files(list, file_base_name):
    number = 1
    list_of_files = []
    for url_page in list:
        create_file_with_url_content(url_page, file_base_name.format(number), dir)
        list_of_files.append('category_page_data_{}.txt'.format(number))
        number += 1
    return list_of_files

list_of_files = put_url_data_into_files(list_of_categories() + list_of_multiple_pages, 'category_page_data_{}.txt')

list_of_books_without_first_section = []
for file in list_of_files:
    file = dir + file
    open_file = open(file, 'r')
    individual_counter = 0
    for line in open_file.readlines():               
        match = re.search(pattern='(?<=<h3><a href="../../../).*(?=" )', string=line)
        if match:
            list_of_books_without_first_section.append(match.group())
            individual_counter += 1
        results_number_match = re.search(pattern='(?<=<strong>).*(?=</strong> results)', string=line)
        if results_number_match:
            results = results_number_match.group()
        pages_match_list = []
    open_file.close()

book_number = 1
for book in list_of_books_without_first_section:
    create_file_with_url_content('https://books.toscrape.com/catalogue/' + book, 'book_{}.txt'.format(book_number), book_htmls_dir)
    book_number += 1 


