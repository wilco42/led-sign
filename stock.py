from datetime import date
import lib.image as image
#import lib.stock as stock

#stock_info = stock.get_stock_info('WDAY')
#print (stock_info)

stock_info = {'symbol': 'WDAY', 'current_price': 238.74, 'day_diff': -7.65, 'percent': -3.10}

card = image.initImage()
# ticker
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = stock_info['symbol'] , offset = (1, 1));

# current price
current = stock_info['current_price'].split(".")
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = current[0], offset = (1, 8));
image.point([(13, 1)], fill = (200, 200, 200))
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = current[1], offset = (18, 8));

# day's diff
image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '7', offset = (43, 1));
image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '65', offset = (50, 1));

# percent diff
image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '3', offset = (43, 8));
image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '10%', offset = (49, 8));
card.save('cards/stock.png')
