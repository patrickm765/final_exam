# this will only change the clours to essentially black and grey

from PIL import Image

# Open the image
image = Image.open("Colors.png")

# Get the width and height of the image
width, height = image.size

#image size = h = 532 and w = 541


for x in range(width):
    for y in range(height):
        
        old_color = image.getpixel((x, y))

        # Change the color (e.g., invert the RGB values)
        Update1_color = tuple(245 - value for value in old_color)

        # Set the new color for the pixel
        image.putpixel((x, y), Update1_color)


image.save("Update1.png")