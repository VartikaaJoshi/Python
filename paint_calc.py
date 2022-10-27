
import math
def paint_calc(height, width, cover):

    paint = (height * width) / cover
    paint_needed = round(paint)

    print(f"Paint needed {paint_needed}")



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


