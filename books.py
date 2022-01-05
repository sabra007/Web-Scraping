from bs4 import BeautifulSoup
import requests
import json


def getHTML(url):
    response = requests.get(url)
    return response.text


book_data = []

for x in range(1,51):
    html = getHTML(f"http://books.toscrape.com/catalogue/page-{x}.html")
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('article', attrs = {'class':'product_pod'})
    for row in rows:

        title = row.find('h3').find('a').attrs['title']
        price = row.find('div', attrs = {'class':'product_price'}).find('p', attrs = {'class':'price_color'}).text.strip("Â£")
        
        book_data.append({'title': title, 'price': price})


books = json.dumps(book_data)

with open('books.json', 'w') as j_file:
    j_file.write(books)