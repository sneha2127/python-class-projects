# Resize Image using Pillow

from PIL import Image

img = Image.open("img.jpg")

# Resize image
# resize = img.resize((500,300))

# resize.save("resize.png")



def resize_img(img,percentage):
    resize_width = int(img.width * percentage)
    resize_height = int(img.height * percentage)
    resize = img.resize((resize_width,resize_height))
    resize.save("resize.png")


user_percentage = int(input("Enter percentage: ")) / 100
resize_img(img,user_percentage)
