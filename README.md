This API is supposed to return the HTML element that contains a given text
string on a given web page. The API has an endpoint that takes the URL and
text search string as arguments and stores them in a database.
If a query already exists in the database, then it should return the stored
value rather than re-scraping the website. If the web page has more than one
matching element, then the last element should be returned from the API.

I have decided to use fastapi because I think it will be faster than django
This API is written in python and has been written by Husayn Esmail.

The due date for this project is May 11, 2022. 


To start the virtual environment:
source pyapi/bin/activate

To leave the virtual environment: 
deactivate