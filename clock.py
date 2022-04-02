from datetime import date, datetime
import lib.image as image
import lib.constant as constant

# get date and time
time_object = datetime.now().time()
today_object = date.today()
time = time_object.strftime('%-I %M')
ampm = time_object.strftime("%p")
day = today_object.strftime('%a %b %-d').upper()

# do the math to center the time
time_length = len(time)

# in this font, the colon is rendered 1 pixel too low, so let's draw it separately
if (time_length == 4):
    time_offset = round((constant.PIXEL_COLS - constant.CHARACTER_WIDTH * (time_length + 2) ) / 2) - 1
    colon_offset = time_offset + constant.CHARACTER_WIDTH
    ampm_offset = time_offset + constant.CHARACTER_WIDTH * time_length + 3
else:
    time_offset = round((constant.PIXEL_COLS - constant.CHARACTER_WIDTH * (time_length + 2) ) / 2) - 2
    colon_offset = time_offset + constant.CHARACTER_WIDTH * 2
    ampm_offset = time_offset + constant.CHARACTER_WIDTH * time_length + 3

# do the math to center the date
day_length = len(day)

if (day_length == 10):
    day_offset = round((constant.PIXEL_COLS - constant.SMALL_CHARACTER_WIDTH * (day_length) ) / 2) + 1
else:
    day_offset = round((constant.PIXEL_COLS - constant.SMALL_CHARACTER_WIDTH * (day_length) ) / 2)

clock = image.initImage()
image.drawText(clock, font = "fonts/5x8.pil", color = (50, 50, 255), text = day, offset = (day_offset, 19));
image.drawText(clock, font = "fonts/7x13.pil", color = (200, 200, 200), text = time, offset = (time_offset, 4));
image.drawText(clock, font = "fonts/7x13.pil", color = (200, 200, 200), text = ampm, offset = (ampm_offset, 4));
image.drawText(clock, font = "fonts/7x13.pil", color = (200, 200, 200), text = ':', offset = (colon_offset, 3));
clock.save('cards/clock.png')
