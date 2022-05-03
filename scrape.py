import requests
import re
r = requests.get('https://www.webscraper.io/test-sites/tables')
from bs4 import BeautifulSoup
print(r)

soup = BeautifulSoup(r.content, 'html.parser')
longstring = soup.prettify()

divided = longstring.split('\n')
# This finds the string, now how do we get what's around it?
the_found = []
count = 0
for divide in divided:
    print(divide,',')
    j = re.findall("larry",divide.lower())
    if j != []:
        the_found.append(divide)
    count += 1


if the_found != []:
    print("THE LAST ONE: ", the_found[-1])