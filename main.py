# if you want to scrape a website:
#1. Use the API
#2. HTML web Scraping using some tool like bs4

#step 0: Install all the requirements
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


#step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)


# Step 3: HTML Tree traversal
# 
# commonly used types of objects:
# 1. Tag / print(type(title))
# 2. NavigableString / print(type(title.string))
# 3. BeautifulSoup / print(type(soup))
# 4. Comment

# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))



#  get the title of the HTML page
title = soup.title

#  Get all the paragraphs from the HTML page
paras = soup.find_all('p')
# print(paras)

#  Get all the anchors from the HTML page
anchors = soup.find_all('a')
all_links = set()
# print(anchors)

# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)


# Get first element in the HTML page
print(soup.find('p'))

# Get classes of any element in the HTML page
print(soup.find('p')['class'])

# find all the elememts with class lead
print(soup.find_all("p" , class_="lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())

# print(soup.get_text())


navbarsupportedContend =  soup.find(id='__next')
# .content - A tag's children are available as a list 
# .children - A tag's children are available as a generator
for elem in navbarsupportedContend.children:
    print(elem)

for item in navbarsupportedContend.stripped_strings:
    print(item)

for item in navbarsupportedContend.parents:
    print(item.name)



# print(navbarsupportedContend.next_sibling.next_sibling)
# print(navbarsupportedContend.previous_sibling.previous_sibling)


elem = soup.select('.modal-footer')
print(elem)