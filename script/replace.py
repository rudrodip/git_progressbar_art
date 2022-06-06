import re

def replace_at_index(text, coord):
    x, y, z = coord
    pat = re.compile(fr'translate\({y}, 0\).+?rect.+?y=.+?{x}.+?data-level=\"(\d+)', re.S)
    new = pat.search(text)
    index = new.span(1)[0]
    text = text[:index] + str(z) + text[index + 1:]
    return text

def replace_html(html, coords):
    text = html
    pattern = re.compile(r'data-level=\"\d+\"', re.S)
    text = pattern.sub("data-level=\"0\"", text)
    for coord in coords:
        text = replace_at_index(text, coord)
    return text