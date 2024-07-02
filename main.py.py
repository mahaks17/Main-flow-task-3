import requests
from bs4 import BeautifulSoup

url= 'https://realpython.com/python-web-scraping-practical-introduction/'

reponse= requests.get(url)

if reponse.status_code == 200:
    soup= BeautifulSoup(reponse.text, 'html.parser')

    page_text=soup.get_text()

    links=[a['href']for a in soup.find_all('a',href=True)]

    images=[img['src']for img in soup.find_all('img',src=True)]

    print("page text:")
    print(page_text)

    print("\nlinks:")
    for link in links:
        print(link)

    print("\nimages:")
    for image in images:
        print(image)
else:
    print(f"failed to retrieve the web page. status code:{reponse.status_code}")