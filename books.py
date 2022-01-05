from bs4 import BeautifulSoup
import requests
import json
import csv

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


# keys = book_data[0].keys()

# with open('books.csv', 'w') as csv_file:
#     dict_writer = csv.DictWriter(csv_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(book_data)

