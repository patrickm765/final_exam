# Question 2 part 2

from PIL import Image
import csv

images = ["Colors.png", "Update1.png", "Black.png"]
output = ["colors_pixel_values.csv", "update1_pixel_values.csv", "black_pixel_values.csv"]

def save_pixel_values(self, output):
    
    image = Image.open(self)

    
    width, height = image.size

    # CSV file creation
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        
        csvwriter.writerow(['X', 'Y', 'R', 'G', 'B'])

        
        for x in range(width):
            for y in range(height):
                
                pixel = image.getpixel((x, y))
                
                
                csvwriter.writerow([x, y, *pixel])

for self, output_csv in zip(images, output):
    save_pixel_values(self, output)