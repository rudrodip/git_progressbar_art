import requests

def page_content(link):
    try:
        page = requests.get(link)
    except:
        return "no url"
    return page.text


# it just returs the text version of the github profile page