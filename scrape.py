# OLD

import requests
# from bs4 import BeautifulSoup
# [TODO]
# optimize this code and clean it up
# ensure it does't use two while loops
# the webpage that I'm scraping at the moment (converted to text)
# [TODO]: rename "r" to html_string
url = "https://www.studytonight.com/python/web-scraping/find-tags-with-beautifulsoup"
# gets the html from the given url and converts it to text
r = requests.get(url).text
# soup = BeautifulSoup(r, 'html.parser')

# finds the last occurrence of the string starting with the first character.
# checks the original string in lowercase against the desired string in lowercase.
# converting allows searching case insensitive
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

# how to do it in one while loop:
'''
    # NOTE THIS HASN'T BEEN TESTED
    # The way to do this in a single while loop (while maintaining) the same
    # concept is to do it like this:
    # recalling that x stores the index of the first letter of the desired string
    start_ind = x
    end_ind = x
    # both start from the found character
    start = r[x]
    end = r[x]
    # determines whether the start and end of the element has been found
    found_start = false
    found_end = false
    while (!found_start and !found_end):
        # moves start_ind to the left until the start is found
        if (start != "<"):
            start_ind -= 1
            start = r[start_ind]
        else:
            found_end = true

        # moves end_ind to the right until the end is found
        if end != ">":
            end_ind += 1
            end = r[end_ind]
        else:
            found_end = true
'''

# searches till it finds the next closing tag.
while end != ">":
    end_ind += 1
    end = r[end_ind]

# prints the final result.
print(r[start_ind:end_ind+1])
