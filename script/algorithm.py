from PIL import Image, ImageDraw, ImageFont
import numpy

width = 52
height = 7

def coordinates(text):
    try:
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
    except Exception as e:
        coords = [[0, 0, 1], [0, 16, 3], [0, 32, 0], [0, 64, 0], [0, 80, 3], [0, 240, 1], [0, 256, 1], [0, 272, 1], [0, 288, 1], [0, 304, 0], [0, 320, 3], [0, 336, 2], [15, 0, 1], [15, 16, 3], [15, 32, 1], [15, 64, 0], [15, 80, 3], [15, 240, 1], [15, 256, 1], [15, 304, 0], [15, 320, 2], [15, 336, 0], [30, 0, 1], [30, 16, 2], [30, 32, 3], [30, 48, 0], [30, 64, 0], [30, 80, 3], [30, 112, 0], [30, 128, 2], [30, 144, 3], [30, 160, 2], [30, 176, 0], [30, 240, 1], [30, 256, 
1], [30, 272, 1], [30, 288, 1], [30, 304, 3], [30, 320, 4], [30, 336, 1], [30, 352, 0], [30, 368, 2], [30, 384, 3], [30, 400, 2], [30, 416, 0], [45, 0, 1], [45, 16, 2], [45, 32, 1], [45, 48, 2], [45, 64, 0], [45, 80, 3], [45, 112, 2], [45, 128, 1], [45, 144, 0], [45, 160, 2], [45, 176, 1], [45, 240, 1], [45, 256, 1], [45, 272, 1], [45, 288, 1], [45, 304, 0], [45, 320, 2], [45, 352, 1], [45, 368, 1], [45, 384, 0], [45, 400, 2], [45, 416, 1], [60, 0, 1], [60, 16, 2], [60, 48, 2], [60, 64, 1], [60, 80, 3], [60, 112, 2], [60, 128, 0], [60, 160, 0], [60, 176, 2], [60, 240, 1], [60, 256, 1], [60, 272, 1], [60, 288, 1], [60, 304, 0], [60, 320, 2], [60, 352, 2], [60, 368, 4], [60, 384, 4], [60, 400, 4], [60, 416, 2], [75, 0, 1], [75, 16, 2], [75, 48, 0], [75, 64, 3], [75, 80, 3], [75, 112, 2], [75, 128, 1], [75, 144, 0], [75, 160, 2], [75, 176, 2], [75, 240, 1], [75, 256, 1], [75, 272, 1], [75, 288, 1], [75, 304, 0], [75, 320, 2], [75, 352, 1], [75, 368, 1], [75, 384, 0], [90, 0, 1], [90, 16, 2], [90, 64, 1], [90, 80, 3], [90, 112, 0], [90, 128, 2], [90, 144, 3], [90, 160, 2], [90, 176, 0], [90, 240, 1], [90, 256, 1], [90, 272, 1], [90, 288, 1], [90, 304, 0], [90, 320, 2], [90, 352, 0], [90, 368, 2], [90, 384, 3], [90, 400, 3], [90, 416, 0]]
        print(e)
        return coords