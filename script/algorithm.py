from PIL import Image, ImageDraw, ImageFont
import numpy

width = 52
height = 7

def coordinates(text):
    img = Image.new(mode = "RGB", size = (width, height), color= (0, 0, 0))
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(img)
    draw.text((0, -2), text, fill = (255, 255, 255), font=font)
    
    img_data = numpy.array(img)
    coords = []
    for i in range(height):
        for j in range(width):
            if sum(img_data[i][j]) > 0:
                coords.append([i*15, j*16, int(sum(img_data[i][j])/191)])
    
    return coords


# How this algorithm works is pretty simple (its not an algorithm though 😅)

#     github progress bar has 7 rows and 52 columns (thus is represents 365 days)

# 1. it takes the text and try to create an image of 7x52 size
# 2. then for every pixel in the numpy array of the image, it checks for the pixel that has color (it means the r+g+b value must be greater than 0)
# 3. then it stores those coordinates in the coords array

#     coords array stores coord -> consists of 3 elements
#         1st element is the column number
#         2nd element is the row  number
#         3rd element is the brightless
#                 github progress data-level has 5 level of brightness - 0, 1, 2, 3, 4
#                     thus is only takes the non-zero pixel, so the brightness can be represented as (total rgb value / 191)
#                                 --> this 191 comes from here: 
#                                             255 + 255 + 255 = 765
#                                             765 // 4 = 191 [as 4 level of actual brightless, 0 is for zero-progress, so we dont need that as we deal with only the colored pixel]
                                        
#     then it returns the coords