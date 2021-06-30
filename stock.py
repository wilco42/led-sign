# get stock info
current_price = 42.42
start_price = 39.26
high_price = 44.12
low_price = 38.13


row_value = calculate_row_value(low_price, high_price)
print (row_value)


def calculate_row_value(low_price, high_price):
    total_range = high_price - low_price
    row_value = total_range / 32
    return row_value

def draw_midline():
    if (start_price == low_price):
        midline = False
    else:
        midline = True
    if (midline):
        # draw a dotted line from whereever the start_price dot is
