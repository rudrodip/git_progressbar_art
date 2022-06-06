import re

def replace_html(html, coords):
    text = html
    pattern = re.compile(r'data-level=\"\d+\"', re.S)
    text = pattern.sub("data-level=\"0\"", text)
    
    indexes = []
    
    for coord in coords:
        pat = re.compile(fr'translate\({coord[1]}, 0\).+?rect.+?y=.+?{coord[0]}.+?data-level=\"(\d+)', re.S)
        new = pat.search(text)
        index = new.span(1)[0]
        indexes.append([index, str(coord[2])])
    
    text = list(text)
    for index in indexes:
        text[index[0]] = index[1]
    
    text = ''.join(text)
    return text


                                                                                             
# explaination of "replace_html" function :::
#     1. first it takes the html page as text
#     2. it changes all the data-level to 0 as it represents the brightness, we want to set everything to 0 initially
#     3. it takes all the coordinates as Parameter
#             -> for every single coord 
#                     -> first finds the translate(y ,0) because every week of progress in github is wraped around "<g></g>" and it has style transform(x, 0)
#                     -> then it looks for the y={x}, because every rect in g has a y value that represents the row number of the progress bar
#                     -> then it finds the specific character
#                     -> then it returns the index of that point by .span(1)[0] -> it actually gives the position of the character in the string
#                     -> then index and corresponding brightness for the index is stored in "indexes" array
#                             index = [position, brightness]
                   
#             text is converted to array as string is immutable in python 
#             for every index
#                 -> it changes the index[0] positioned value to index[1]
#             text is then converted to string again
            
#     after the iteration, it returns the text