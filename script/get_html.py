import requests

def page_content(link):
    page = requests.get(link)
    return page.text


# it just returs the text version of the github profile page