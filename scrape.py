import requests
import re
r = requests.get('https://geeksforgeeks.org/python-programming-language/')
from bs4 import BeautifulSoup
print(r)

soup = BeautifulSoup(r.content, 'html.parser')
longstring = soup.prettify()

divided = longstring.split('\n')
# This finds the string, now how do we get what's around it?
the_found = {}
count = 0
for divide in divided:
    j = re.findall("python",divide)
    if j != []:
        the_found[str(count)] = divide
    count += 1

print(the_found)


print("THE LAST ONE: ", list(the_found.values())[-1])