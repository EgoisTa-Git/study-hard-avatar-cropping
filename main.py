from PIL import Image


shift = 50
image = Image.open("example.jpg")
red, green, blue = image.split()
red_shift_1 = red.crop((2 * shift, 0, red.width, red.height))
red_shift_2 = red.crop((shift, 0, red.width - shift, red.height))
new_red = Image.blend(red_shift_1, red_shift_2, 0.5)
blue_shift_1 = blue.crop((0, 0, blue.width - 2 * shift, blue.height))
blue_shift_2 = blue.crop((shift, 0, blue.width - shift, blue.height))
new_blue = Image.blend(blue_shift_1, blue_shift_2, 0.5)
new_green = green.crop((shift, 0, green.width - shift, green.height))
new_example = Image.merge("RGB", (new_red, new_green, new_blue))
new_example.save("new_example.jpg")
new_example.thumbnail((80, 80))
new_example.save("new_example_thumbnail.jpg")
