import requests
import html

def page_content(link):
    page = requests.get(link)
    return page.text