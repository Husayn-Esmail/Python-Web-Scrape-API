import requests
import re
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import lxml

# the webpage that I'm scraping at the moment (converted to text)
r = requests.get('https://www.studytonight.com/python/web-scraping/find-tags-with-beautifulsoup').text
soup = BeautifulSoup(r, 'html.parser')

# selecting the head tag
html_tag = soup.html
# print(html_tag.contents)
# this prints the tag and it's contents and then just the contents alone. i.e. there could be many duplicates of content.
phrase = re.compile("learn", re.IGNORECASE)
the_found = []
for child in html_tag.descendants:
    try:
        x = child.find_all(string=phrase)
        if x != []:
            the_found.append(x)
    except:
        if (str(child.string).__contains__(phrase)):
            the_found.append(child)
    # print(child)

print(the_found)

# the given string to be matched















# this just returns all text that are contained in the <p>
# s = re.compile("the")
# regex = "<[a-zA-Z]>+[a-zA-Z]+python+[a-zA-Z]+</[a-zA-Z]>"
# texts = soup.find_all(string=s)
# print(texts)
# texts = soup.find_all(string=regex)
# print(texts)
# start_tags = []
# end_tags = []
# data = []


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Start: <", tag,">")
#         return tag
    
#     def handle_endtag(self, tag):
#         print("End: <", tag,">")
#         return tag
    
#     def handle_data(self,data):
#         print("Data: ", data)
#         return data

# parser = MyHTMLParser()
# i = parser.feed(r)

# print(found)
# longstring = soup.prettify()

# divided = longstring.split('\n')
# # This finds the string, now how do we get what's around it?
# the_found = []
# count = 0
# for divide in divided:
#     print(divide,',')
#     j = re.compile(r"  (\s([a-zA-Z]+\s)+)  ",re.IGNORECASE)
#     x = j.match(divide)
#     the_found.append(x)
#     count += 1


# if the_found != []:
#     print("THE LAST ONE: ", the_found[-1])

