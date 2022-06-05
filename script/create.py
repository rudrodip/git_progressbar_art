import os
from script import get_html, algorithm, replace
    
def main(link, text):
    content = get_html.page_content(link)
    coords = algorithm.coordinates(text)
    replaced_content = replace.replace_html(content, coords)
    return replaced_content