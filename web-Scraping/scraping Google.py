import urllib
import requests
from bs4 import BeautifulSoup
from csv import writer


# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

query = "python books"
query = query.replace(' ', '+')

# add specific query to google link
URL = f"https://google.com/search?q={query}"

headers = {"user-agent": USER_AGENT}  # define header
response = requests.get(URL, headers=headers)

dictCounter = 0
if response.status_code == 200:  # check if succeeded
    soup = BeautifulSoup(response.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                   "title": title,
                    "link": link
                }
            results.append(item)
    for desc in soup.find_all('div', class_='s'):
        descreption = desc.find_all('span')
        if descreption:
            describing_link = descreption[0].text + descreption[1].text
            describing_link = describing_link.replace(',', ' ') #for further process of the file removed all commas in column
        else:
            describing_link = 'N/A' # in case there is no description
        results[dictCounter]['description'] = describing_link
        dictCounter += 1

with open('booksSearch.csv', 'w+', newline='') as csv_file: #create the file with no whitespaces between lines
    csv_writer = writer(csv_file)
    headers1 = ['Title','description', 'Link']
    csv_writer.writerow(headers1)

    for result in results:
        csv_writer.writerow(
            [result['title'], result['description'], result['link']])

print(results)
