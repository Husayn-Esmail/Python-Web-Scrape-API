import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path


def load_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") # linux only
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options)
    start_url = "https://testmysite.io"
    driver.get(start_url)
    print(str(driver.page_source.encode("utf-8")))
    driver.quit()

def comparison(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    s = Service(binary_path)
    driver = webdriver.Chrome(service=s,options=chrome_options)
    driver.get(url)
    with open("chrome.txt", "w") as file:
        file.write(driver.page_source)
        file.write(str(type(driver.page_source)))
    with open("chromeutf8.txt", "w") as file:
        file.write(str(driver.page_source.encode("utf-8")))
    driver.quit()
    regular_get = requests.get(url).text
    with open("get.txt", "w") as file:
        file.write(regular_get)
    print("complete")

    


def get_html(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html)
    print(type(soup))

if __name__ == "__main__":
    # url = input("enter a url: ")
    # get_html(url)
    # load_chrome()
    comparison("https://testmysite.io")