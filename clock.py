from datetime import date
import lib.image as image

today = date.today()
time = today.strftime('%-I:%M')
ampm = today.strftime("%p")
day = today.strftime('%a %b %-d').upper()

clock = image.initImage()
image.drawText(clock, font = "fonts/5x8.pil", color = (50, 50, 255), text = day, offset = (8, 21));
image.drawText(clock, font = "fonts/7x13.pil", color = (200, 200, 200), text = time, offset = (6, 6));
image.drawText(clock, font = "fonts/7x13.pil", color = (200, 200, 200), text = ampm, offset = (44, 6));
clock.save('cards/clock.png')
