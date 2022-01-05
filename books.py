from bs4 import BeautifulSoup
import requests
import json
import csv
import pandas as pd

def getHTML(url):
    response = requests.get(url)
    return response.text


book_data = []

for x in range(1,51):
    html = getHTML(f"http://books.toscrape.com/catalogue/page-{x}.html")
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('article', attrs = {'class':'product_pod'})

    for article in articles:

        title = article.find('h3').find('a').attrs['title']
        price = article.find('div', attrs = {'class':'product_price'}).find('p', attrs = {'class':'price_color'}).text.strip("Â£")
        rating = ''.join(article.find('p')['class']).strip()[11:]

        book_data.append({'title': title, 'price': price, 'rating': rating})


books = json.dumps(book_data)

with open('books.json', 'w') as j_file:
    j_file.write(books)


with open('books.json', encoding='utf-8-sig') as f_input:
    df = pd.read_json(f_input)

df.to_csv('books.csv', encoding='utf-8', index=False)

