from cgitb import html
from script import get_html, algorithm, replace
    
def main(link, text):
    content = get_html.page_content(link)
    try:
        coords = algorithm.coordinates(text)
        replaced_content = replace.replace_html(content, coords)
    except:
        return content
    return replaced_content


# it imports all the functions from the directory and calls them
# 1. first it gets the html page via "get_html.page_content"
# 2. it gets all the coords for the text via "algorithm.coordinates"
# 3. it replaces all the coords with the programmatically generated coordinates
# 4. then it gives that coordinates to the "replace.replace_html" to get the new html
# 5. then it returns that html file as text