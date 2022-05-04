import requests
# from bs4 import BeautifulSoup
# [TODO]
# optimize this code and clean it up
# ensure it does't use two while loops
# the webpage that I'm scraping at the moment (converted to text)
r = requests.get('https://www.studytonight.com/python/web-scraping/find-tags-with-beautifulsoup').text
# soup = BeautifulSoup(r, 'html.parser')

# finds the last occurrence of the string starting with the first character.
# checks the original string in lowercase against the desired string in lowercase.
x = r.lower().rfind("learn")
# starting and end indices
start_ind = x
end_ind = x
# start and end character
start = r[x]
end = r[x]
# searches backwards till it finds the opening tag
while start != "<":
    start_ind -= 1
    start = r[start_ind]

# searches till it finds the next closing tag.
while end != ">":
    end_ind += 1
    end = r[end_ind]

# prints the final result.
print(r[start_ind:end_ind+1])
