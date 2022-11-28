from bs4 import BeautifulSoup as bs
import codecs
import requests
import re
import unidecode
from statistics import mean


url = 'https://www.muztorg.ru/category/bas-gitary?in-stock=1&pre-order=1'
pagen_num=1
pagen=f'&page={pagen_num}'
newUrl=url+pagen
response = requests.get(newUrl)
soup = bs(response.content, 'html.parser')
title = soup.find('h1', class_='category-head__title')
item_count = soup.find('span', class_='category-head__badge')
print("Заголовок:",title.text)
print("Количество товара:",item_count.text)
prices = soup.find_all('p', class_='price')
price_array=[]
for price in prices:
    result = unidecode.unidecode(price.text)
    result=result.replace(' ','').replace('\n','').replace('r.','')
    price_array.append(result)
price_array=list(map(int, price_array))
print("Минимальная стоимость товара:",min(price_array))
print("Максимальная стоимость товара:",max(price_array))
print("Средняя стоимость товара:",mean(price_array))
print("Общая стоимость товара:",sum(price_array))
print("Список товара:")
pages=soup.find_all('ul', class_='pagination')
page_array=[]
for page in pages:
    result = unidecode.unidecode(page.text)
    result = result.replace('\n', ' ').replace('>>', ' ').strip()
    page_array.append(result)
if pages ==[]:
    page_num=1
else:
    page_num=page_array[0].split()[len(page_array[0].split())-1]
n=0
for num in range(1,int(page_num)+1):
    newUrl=url+f'&page={num}'
    response = requests.get(newUrl)
    soup = bs(response.content, 'html.parser')
    items = soup.find_all('section', class_='product-thumbnail')
    for n, i in enumerate(items, start=n+1):
        itemName = i.find('div', class_='title').text.strip()
        itemPrice = i.find('p', class_='price').text.replace('р.', '').strip()
        
        print(f'{n}: {itemName} за {itemPrice}₽')
