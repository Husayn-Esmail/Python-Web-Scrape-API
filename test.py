import requests
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    print(soup)

if __name__ == "__main__":
    url = input("enter a url: ")
    get_html(url)
