import re

def replace_at_index(text, coord):
    x, y, z = coord
    pat = re.compile(fr'translate\({y}, 0\).+?rect.+?y=.+?{x}.+?data-level=\"(\d+)', re.S)
    new = pat.search(text)
    index = new.span(1)[0]
    text = list(text)
    text[index] = str(z)
    text = ''.join(text)
    return text

def replace_html(html, coords):
    text = html
    pattern = re.compile(r'data-level=\"\d+\"', re.S)
    text = pattern.sub("data-level=\"0\"", text)
    for coord in coords:
        text = replace_at_index(text, coord)
    return text





# this file does a lot of things

# it uses REGEX for finding out the correct rect (in the page source of github profile, every single box on the github progressbar, its wrapped with "<rect></rect>")

# explaination of "replace_at_index" function ::::
    
#     1. takes the text of the html file and the specific coord (coord = [x, y, z] -> x = row, y = col, z = brightness)
#     2. uses a pattern of regex to find out the position of the box
#         -> first finds the translate(y ,0) because every week of progress in github is wraped around "<g></g>" and it has style transform(x, 0)
#         -> then it looks for the y={x}, because every rect in g has a y value that represents the row number of the progress bar
#         -> then it finds the specific character (the default brightless is set to 0 in the "replace_html" function)
#         -> then it returns the index of that point by .span(1)[0] -> it actually gives the position of the character in the string
#         -> then text is converted to list and the specific character is set to the brightness
#                     -> here we're using the list because in python, string is immutable
#         -> then it converts the list to string again and
#                                                 -> return it
                                                
                                                
                                                
# explaination of "replace_html" function :::
#     1. first it takes the html page as text
#     2. it changes all the data-level to 0 as it represents the brightness, we want to set everything to 0 initially
#     3. it takes all the coordinates as Parameter
#             -> for every single coord in calls the replace_at_index function to change the brightness of the rect
#             -> then it sets text to the replaced text
            
#     after the iteration, it returns the text