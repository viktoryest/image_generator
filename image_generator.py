from PIL import Image, ImageDraw, ImageFont


def image_function(text, file_name, background_colour, text_colour, necessary_font, font_size, w_padding, h_padding):
    img = Image.new('RGBA', (2, 2), color=background_colour)
    font = ImageFont.truetype(necessary_font, font_size)
    draw = ImageDraw.Draw(img)
    text_size = draw.textsize(text, font)
    image_size = (text_size[0] + w_padding * 2, text_size[1] + h_padding * 2)

    img = img.resize(image_size)
    draw = ImageDraw.Draw(img)
    draw.text((w_padding, h_padding), text, text_colour, font)
    img.save(file_name)
