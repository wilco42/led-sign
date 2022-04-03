from datetime import date
import lib.image as image
import lib.constant as constant
import lib.stock as stock
import math

def draw_right_string(image, card, string, offset_y, percent=False):
    font_width = 5
    if (string < 0):
        string_color = (200, 0, 0)
    else:
        string_color = (0, 200, 0)

    new_string = '{0:.2f}'.format(abs(string))
    if (percent):
        new_string = new_string + '%'
        cents_offset = 4
        dot_offset = (font_width + 1) * 3 - 2
    else:
        cents_offset = 3
        dot_offset = (font_width + 1) * 2
    new_string_length = len(new_string)
    new_string_x = constant.PIXEL_COLS - (new_string_length * font_width) + 4
    new_string_components = new_string.split(".")
    image.drawText(card, font = "fonts/5x8.pil", color = string_color, text = new_string_components[0], offset = (new_string_x, offset_y));
    card.putpixel((constant.PIXEL_COLS - dot_offset, offset_y + font_width + 1), string_color)
    image.drawText(card, font = "fonts/5x8.pil", color = string_color, text = new_string_components[1], offset = (new_string_x + (font_width + 1) * (new_string_length - cents_offset), offset_y));


card = image.initImage()
stock_info = stock.get_stock_info('WDAY')
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = stock_info['symbol'] , offset = (1, 1));

# current price
current = str(stock_info['current_price']).split(".")
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = current[0], offset = (1, 8));
card.putpixel((16, 14), (200, 200, 200))
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = current[1], offset = (18, 8));

# day's diff
draw_right_string(image, card, stock_info['day_diff'], 1)

# percent diff
draw_right_string(image, card, stock_info['percent'], 8, percent=True)

# graph
index = stock_info['total_rows'] / constant.PIXEL_COLS
for x in range(constant.PIXEL_COLS):
    first_pixel = False
    current_index = math.floor((x + 1) * index)
    if (current_index >= stock_info['total_rows']):
        current_index -= 1
    time_price = round(stock_info['data'][4][current_index], 2)
    if (time_price >= stock_info['previous_close']):
        first_time_color = (0, 255, 0)
        time_color = (0, 175, 0)
    else:
        first_time_color = (255, 0, 0)
        time_color = (175, 0, 0)
    for y in range(16):
        current_offset = (x, y+16)
        current_pixel_price = stock_info['max'] - y * stock_info['increment']
        if (time_price >= current_pixel_price):
            if (first_pixel == False):
                card.putpixel(current_offset, first_time_color)
                first_pixel = True
            else:
                card.putpixel(current_offset, time_color)

card.save('cards/stock_' + stock_info['symbol'] + '.png')
