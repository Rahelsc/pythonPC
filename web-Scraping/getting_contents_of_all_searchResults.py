import requests
from bs4 import BeautifulSoup

html_file = open('C:\\Users\\rahel\\Google Drive\\אריאל\\שנה א\\סמסטר ב\\python\\booksSearch.html', 'r')
reading = html_file.readlines()
count = 1
for line in reading:
    if 'https://' in line: # to make sure we're only working with link
        index_start_link = line.find('http') # cutting start of url
        index_end_link = line.find('<', index_start_link) # end of url
        url = line[index_start_link:index_end_link] # actual slicing
        print(url) # just to make sure everything is runing correctly
        response = requests.get(url) # basic scraping of html content
        beauty = BeautifulSoup(response.text, 'html.parser')
        b = beauty.body.text.replace('\n', '') # reading contents as text
        text_file = open(f"output{count}.txt", "w", encoding="utf-8") # writing to file - name changes each iteration of loop
        text_file.write(b)
        text_file.close()
        count += 1
