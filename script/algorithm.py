from PIL import Image, ImageDraw, ImageFont
import numpy

width = 52
height = 7

def coordinates(text):
    img = Image.new(mode = "RGB", size = (width, height), color= (0, 0, 0))
    font = ImageFont.truetype("arial.ttf", 9)
    draw = ImageDraw.Draw(img)
    draw.text((0, -2), text, fill = (255, 255, 255), font=font)
    
    img_data = numpy.array(img)
    coords = []
    for i in range(height):
        for j in range(width):
            if sum(img_data[i][j]) > 0:
                coords.append([i*15, j*16, int(sum(img_data[i][j])/191)])
                
    return coords