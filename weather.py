from datetime import date
import lib.image as image
import bitmaps.weather_images as bitmap

today = date.today()
day = today.strftime('%a').upper()
temp_high = '101°'
temp_low = '42°'
temp_current = '77°'

weather = image.initImage()
image.drawText(weather, font = "fonts/5x8.pil", color = (200, 200, 200), text = temp_high, offset = (44, 17));
image.drawText(weather, font = "fonts/5x8.pil", color = (200, 200, 200), text = temp_low, offset = (44, 25));
image.drawText(weather, font = "fonts/6x12.pil", text = temp_current, offset = (2, 14));
image.drawText(weather, font = "fonts/5x8.pil", color = (255, 255, 150), text = day, offset = (2, 25));
image.drawBitmap(weather, bitmap.sun, (255, 255, 0))
weather.save('cards/weather.png')
