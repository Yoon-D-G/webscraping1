import os
import re

complete_dictionary = {}
counter = 0
line_number = 0
number_of_files = 0
titles_list = []
for book_html_file in os.listdir('/home/garrotero/webscraping/book_htmls'):
    number_of_files += 1
    open_book_file = open('/home/garrotero/webscraping/book_htmls/' + book_html_file, 'r')
    for line in open_book_file.readlines():
        if '| Books to Scrape - Sandbox' in line:
            title = line.split('|')[0].strip()
            complete_dictionary[title] = {
        'URL': None, 
        'UPC': None, 
        'Product_Type': 'Books', 
        'Price_excl_tax': None,
        'Price_incl_tax': None,
        'Tax': 0,
        'Availability': None,
        'Number_of_reviews': 0,
        'Product_description': None 
            }
        if 'url' in line:
            match = re.search(pattern='(?<=<url=).*(?=>)', string=line)
            if match:
                complete_dictionary[title]['URL'] = match.group()
        if 'UPC' in line:
            match = re.search(pattern='(?<=<th>UPC</th><td>).*(?=</td>)', string=line)
            if match:
                complete_dictionary[title]['UPC'] = match.group()
        if 'Price (excl. tax)' in line:
            match = re.search(pattern='(?<=</th><td>).*(?=</td>)', string=line)
            if match:
                complete_dictionary[title]['Price_excl_tax'] = match.group()
        if 'Price (incl. tax)' in line:
            match = re.search(pattern='(?<=</th><td>).*(?=</td>)', string=line)
            if match:
                complete_dictionary[title]['Price_incl_tax'] = match.group()   
        if 'In stock' in line:
            match = re.search(pattern='(?<=<td>).*(?=</td>)', string=line)
            if match:
                complete_dictionary[title]['Availability'] = match.group()
        if '</p>' in line and len(line) > 40:
            match = re.search(pattern='(?<=<p>).*(?=</p>)', string=line)
            if match:
                complete_dictionary[title]['Product description'] = match.group()
                    

dict_file = open('/home/garrotero/webscraping/book_dict.txt', 'w')
dict_file.write(str(complete_dictionary))
dict_file.close()



# open_book_file = open('/home/garrotero/webscraping/book_htmls/book_html_701', 'r')
# for line in open_book_file.readlines():
#     if '| Books to Scrape - Sandbox' in line:
#         # complete_dictionary[line.split('|')[0].strip()] = book_html_file
#         complete_dictionary.append(([line.split('|')[0].strip()]))


# lsta = []
# def lambda1(item):
#     number = int(item[1].split('_')[2])
#     lsta.append((number, item[0]))
#     return item[1].split('_')[2]


# list1 = []
# def lsty(lst):
#     for i in lst:
#         list1.append(i)

# lst = [1, 2, 3]
# lsty(lst)
# #print(list1)    


# new_dict = [(k, v) for k, v in sorted(complete_dictionary.items(), key=lambda1)]
# for i in enumerate(sorted(lsta), 1):
#     print(i)




#print(new_dict)
# print(len(new_dict))
# 'The Smitten Kitchen Cookbook': 'book_html_931'





# match = re.search(pattern='(?<=<h3><a href="../../../).*(?=" )', string=line)

# match = re.search(pattern='/^(.*?) | Books to/', string=line.strip())

# complete_dictionary = {'<title>':
#     {
#         'Title': '<title>', 
#         'URL': '<url>', 
#         'UPC': '<UPC>', 
#         'Product_Type': '<Product type>', 
#         'Price_excl_tax': '<price exc tax>',
#         'Price_incl_tax': 'price inc tax',
#         'Tax': '<tax>',
#         'Availability': '<availability>',
#         'Number_of_reviews': '<number of reviews>',
#         'Product_description': '<product description>' 
#     },
#     '<title2>':
#     {
#         'Title': '<title>', 
#         'URL': '<url>', 
#         'UPC': '<UPC>', 
#         'Product_Type': '<Product type>', 
#         'Price_excl_tax': '<price exc tax>',
#         'Price_incl_tax': 'price inc tax',
#         'Tax': '<tax>',
#         'Availability': '<availability>',
#         'Number_of_reviews': '<number of reviews>',
#         'Product_description': '<product description>'  
#     }
# }