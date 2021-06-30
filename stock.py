from datetime import date
import lib.image as image
import lib.stock as stock

card = image.initImage()
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = 'WDAY' , offset = (1, 1));

image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = '238', offset = (1, 8));
image.drawText(card, font = "fonts/5x8.pil", color = (200, 200, 200), text = '74', offset = (18, 8));

image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '7', offset = (43, 1));
image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '65', offset = (50, 1));

image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '3', offset = (43, 8));
image.drawText(card, font = "fonts/5x8.pil", color = (200, 0, 0), text = '10%', offset = (49, 8));
card.save('cards/stock.png')
