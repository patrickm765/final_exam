from PIL import Image


_image = Image.open("Update1.png")
black_pic = Image.open("Black.png")


width, height = _image.size


for x in range(width):
    for y in range(height):
        
        pixel_value = _image.getpixel((x, y))
        
       
        black_pic.putpixel((x, y), pixel_value)


black_pic.save("Update2.png")