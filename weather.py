from datetime import date
import lib.image as image

today = date.today()
day = today.strftime('%a').upper()
temp_high = '101°'
temp_low = '42°'
temp_current = '77°'

weather = image.initImage()
image.drawText(weather, font = "fonts/5x8.pil", color = (200, 200, 200), text = temp_high, offset = (44, 13));
image.drawText(weather, font = "fonts/5x8.pil", color = (200, 200, 200), text = temp_low, offset = (44, 22));
image.drawText(weather, font = "fonts/7x13.pil", text = temp_current, offset = (2, 7));
image.drawText(weather, font = "fonts/5x8.pil", color = (255, 255, 150), text = day, offset = (2, 22));
weather.save('cards/weather.png')
