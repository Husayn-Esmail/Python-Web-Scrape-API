This API is supposed ot return the HTML element that contains a given text
string on a given web page. The API has an endpoint that takes the URL and
text search string as arguments and stores them in a database.
If a query already exists in the database, then it should return the stored
value rather than re-scraping the website. If the web page has more than one
matching element, then teh last element should be returned from the API.

This API is written in python and has been written by Husayn Esmail.
