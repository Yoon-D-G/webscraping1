
import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup

dictionary = {}
counter = 1
open_book_list = open('complete_book_list_urls.txt', 'r')
for book_url in open_book_list.readlines():
    book_url = str(book_url).strip()
    soup = str(get_html_content(book_url))
    print(soup)
    book_file = open('/home/garrotero/webscraping/book_htmls/book_html_{}'.format(counter), 'w')
    book_file.write(soup)
    book_file = open('/home/garrotero/webscraping/book_htmls/book_html_{}'.format(counter), 'a')
    book_file.write('<url={}>'.format(book_url))
    book_file.close()
    counter += 1
    print(f'iteration {counter}')
open_book_list.close()


 
            
            

            
                
            
            

            
                
            
            

            
                
            
            

            
                
            
            

            
                
