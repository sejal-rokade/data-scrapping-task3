import requests as rq
from bs4 import BeautifulSoup

bUrl='https://books.toscrape.com/'

bHeader={
   'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

bResp=rq.get(url=bUrl,headers=bHeader)

bSoup=BeautifulSoup(bResp.content,'html.parser')

books=bSoup.find('div',attrs={'class':'h1'})

print(f'books={books}')

bookNames= bSoup.find_all('h3')

print('bookNames',bookNames)

bookTitle=[]
for Title in bookNames:
   print('Title',Title.find('a')['title'])
   #bookTitle.append(Title.find('a')['title'])

#print('bookTitle',bookTitle)


priceList=bSoup.find_all('p',attrs={'class':'price_color'})
for price in priceList:
   print('price',price.text)

RatingList=bSoup.find_all('p',attrs={'class':'star-rating'})
for rating in RatingList:
   print('rating',rating['class'][1])
