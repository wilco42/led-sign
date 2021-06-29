from PIL import Image, ImageFont, ImageDraw

def initImage():
    image = Image.new(mode = "RGB", size=(64,32))
    return image

# use a bitmap font
def drawText(image, font = "../fonts/5x8.pil", color = (255, 255, 255), text = "hello", filename = "test.png", offset = (0, 0)):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load(font)
    draw.text(offset, text, font = font, fill = color)
    return image

def resizeImage(filename):
    with Image.open(filename) as im:
        im_resized = im.resize((64, 32))
    return im_resized
